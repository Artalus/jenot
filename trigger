#!/usr/bin/env python3
import requests
from requests.api import head

JENKINS = 'http://localhost:8080'
c = requests.get(f'{JENKINS}/crumbIssuer/api/json').json()['crumb']
print(requests.post(f'{JENKINS}/job/sleep/build', headers={'Jenkins-Crumb':c}).content)
