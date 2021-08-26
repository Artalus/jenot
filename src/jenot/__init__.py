#!/usr/bin/env python3
from __future__ import annotations

from enum import Enum, auto as autoenum
from importlib.resources import files
import json
import platform
import time
from typing import Literal, Optional

import requests
from requests.exceptions import ConnectionError, Timeout
import yaml

from . import log


class IterateDecision(Enum):
    CONTINUE = autoenum()
    SUCCESS = autoenum()
    FAILURE = autoenum()
    CONNECTION_ERROR = autoenum()


def normalize_build_url(url: str, jenkins_base: str) -> str:
    if not jenkins_base.endswith('/'):
        jenkins_base += '/'
    if not url.startswith(jenkins_base):
        url = jenkins_base+url
    if url.endswith('/consoleFull'):
        url = url[:-len('/consoleFull')]
    if url.endswith('/console'):
        url = url[:-len('/console')]
    return url


def iterate(url: str, user: Optional[str], token: Optional[str]) -> tuple[IterateDecision, Optional[str]]:
    try:
        auth = (user, token) if any((user, token)) else None
        resp = requests.get(f'{url}/api/json', auth=auth).json()
    except (ConnectionError, Timeout) as e:
        log.warning(f'connection error: {e}')
        return IterateDecision.CONNECTION_ERROR, None

    yaml_resp = yaml.dump(yaml.load(json.dumps(resp), Loader=yaml.FullLoader))
    log.debug(f'response:')

    try:
        if resp['building']:
            return IterateDecision.CONTINUE, None
        r = resp['result']
        if not r:
            return IterateDecision.CONTINUE, None
        if r == 'SUCCESS':
            return IterateDecision.SUCCESS, resp['url']
        else:
            return IterateDecision.FAILURE, resp['url']
    except Exception as e:
        log.exception(f'failed to parse api response; got this:\n{yaml_resp}')
        raise


def run(JENKINS: str, USER: str, TOKEN: str, url: str) -> tuple[int, str]:
    url = normalize_build_url(url, JENKINS)

    conn_errors = 0
    MAX_CONN_ERRORS = 5
    while conn_errors <= MAX_CONN_ERRORS:
        result, actual_url = iterate(url, USER, TOKEN)
        actual_url = actual_url or url
        if result == IterateDecision.CONNECTION_ERROR:
            conn_errors += 1
        else:
            conn_errors = 0

        if result in (IterateDecision.FAILURE, IterateDecision.SUCCESS):
            pass
        elif result == IterateDecision.CONTINUE:
            to_sleep = 60 * (conn_errors+1)
            time.sleep(to_sleep)
    else:
        log.error(f'Too many ({MAX_CONN_ERRORS}) connection errors, aborting')
        return 1, actual_url


def logo(ext: Literal['auto', 'ico', 'png']) -> str:
    if ext == 'auto':
        ext = 'ico' if platform.system() == 'Windows' else 'png'
    # mypy things joinpath takes Traversable instead of str o_O
    p = files('jenot').joinpath(f'data/logo.{ext}') # type: ignore
    return str(p)
