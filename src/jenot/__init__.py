#!/usr/bin/env python3

import sys
import time

import requests


def run(JENKINS, USER, TOKEN, url) -> int:
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
        print(j)
        if r == 'SUCCESS':
            return 0
        else:
            return 1
