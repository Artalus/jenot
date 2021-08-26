import time
from uuid import uuid4 as uid

import requests

from jenot import IterateDecision, iterate

from util.wait import wait_for_200

QUIET_PERIOD_TIMEOUT=15

def test_iterate_success() -> None:
    # FIXME: currently restarts builds, but looks always for the first one
    # TODO: find by id
    U = uid()
    r = requests.post('http://localhost:8080/job/sleep/buildWithParameters', params=dict(SLEEP=0, UID=U))
    assert r.status_code == requests.codes.created
    wait_for_200('http://localhost:8080/job/sleep/1/api/json', timeout=QUIET_PERIOD_TIMEOUT)
    time.sleep(1)
    B = 'http://localhost:8080/job/sleep/1/'
    it, url = iterate(B, None, None)
    assert it == IterateDecision.SUCCESS
    assert url == B
