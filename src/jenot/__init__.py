#!/usr/bin/env python3
from __future__ import annotations
from importlib.resources import files
import json
import platform
import time
from typing import Literal
import yaml

import requests


def run(JENKINS: str, USER: str, TOKEN: str, url: str) -> tuple[int, str]:
    if not url.startswith(JENKINS):
        url = JENKINS+url
    if url.endswith('/consoleFull'):
        url = url[:-len('/consoleFull')]
    if url.endswith('/console'):
        url = url[:-len('/console')]


    while True:
        j = requests.get(f'{url}/api/json', auth=(USER, TOKEN)).json()
        if j['building']:
            print('sleepin...')
            time.sleep(60)
            continue
        r = j['result']
        if not r:
            continue
        y = yaml.load(json.dumps(j), Loader=yaml.FullLoader)
        print(yaml.dump(y))
        if r == 'SUCCESS':
            return 0, j['url']
        else:
            return 1, j['url']


def logo(ext: Literal['auto', 'ico', 'png']) -> str:
    if ext == 'auto':
        ext = 'ico' if platform.system() == 'Windows' else 'png'
    # mypy things joinpath takes Traversable instead of str o_O
    p = files('jenot').joinpath(f'data/logo.{ext}') # type: ignore
    return str(p)
