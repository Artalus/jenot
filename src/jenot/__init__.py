#!/usr/bin/env python3
from __future__ import annotations

from enum import Enum, auto as autoenum
from importlib.resources import files
import json
import platform
import time
from typing import Literal, NamedTuple, Optional, cast

from meiga import Error, Success, Failure, Result
import requests
from requests.exceptions import ConnectionError, Timeout
import yaml


from jenot import log
from jenot.url import normalize_build_url

class PollResult(NamedTuple):
    result: str

    @property
    def success(self) -> bool:
        return self.result == 'SUCCESS'

class IterateDecision(Enum):
    CONTINUE = autoenum()
    FINISH = autoenum()
    CONNECTION_ERROR = autoenum()
    INTERNAL_ERROR = autoenum()


def iterate(url: str, user: Optional[str], token: Optional[str]) -> tuple[IterateDecision, Optional[PollResult], str]:
    url_to_get = f'{url}/api/json'
    try:
        auth = (user, token) if any((user, token)) else None
        # TODO: add handling for when result is not json (issue #38)
        resp = requests.get(url_to_get, auth=auth).json()
    except (ConnectionError, Timeout) as e:
        log.warning(f'connection error: {e}')
        return IterateDecision.CONNECTION_ERROR, None, url

    yaml_resp = yaml.dump(yaml.load(json.dumps(resp), Loader=yaml.FullLoader))

    refined_url = resp.get('url', url)
    try:
        if resp['building']:
            return IterateDecision.CONTINUE, None, refined_url
        r = resp['result']
        if not r:
            return IterateDecision.CONTINUE, None, refined_url
        result = PollResult(result=r)
        return IterateDecision.FINISH, result, refined_url
    except Exception as e:
        log.exception(f'failed to parse api response from {url_to_get}; got this:\n\n{yaml_resp}\n')
        return IterateDecision.INTERNAL_ERROR, None, refined_url


def run_poll(JENKINS: str, USER: str, TOKEN: str, url: str) -> tuple[Result[PollResult, Error], str]:
    normalized = normalize_build_url(url, JENKINS)
    if normalized.is_failure:
        return Failure(normalized.value), url
    url = cast(str, normalized.unwrap())

    conn_errors = 0
    MAX_CONN_ERRORS = 5
    refined_url = '' # TODO: silly hack to assure mypy the variable is always bound
    while conn_errors <= MAX_CONN_ERRORS:
        decision, result, refined_url = iterate(url, USER, TOKEN)
        if decision == IterateDecision.CONNECTION_ERROR:
            conn_errors += 1
            decision = IterateDecision.CONTINUE
        else:
            conn_errors = 0

        if decision == IterateDecision.FINISH:
            return Success(result), refined_url
        elif decision == IterateDecision.CONTINUE:
            if conn_errors < MAX_CONN_ERRORS:
                time.sleep(60 * conn_errors)
        else:
            raise NotImplementedError(f'unknown decision {decision}')
    else:
        log.error(f'Too many ({MAX_CONN_ERRORS}) connection errors, aborting')
        return Failure('Too many connection errors'), refined_url


def logo(ext: Literal['auto', 'ico', 'png']) -> str:
    if ext == 'auto':
        ext = 'ico' if platform.system() == 'Windows' else 'png'
    # mypy things joinpath takes Traversable instead of str o_O
    p = files('jenot').joinpath(f'data/logo.{ext}') # type: ignore
    return str(p)
