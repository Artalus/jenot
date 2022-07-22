import time
from uuid import uuid4 as uid

from api4jenkins import Jenkins
from api4jenkins.queue import QueueItem
from api4jenkins.build import Build

from jenot import IterateDecision, iterate

from util.wait import wait_for_200

QUIET_PERIOD_TIMEOUT=15

def test_iterate_success() -> None:
    jk = Jenkins('http://localhost:8080')
    U = uid()
    q: QueueItem = jk.build_job('sleep', SLEEP=0, UID=U)
    while not q.get_build():
        time.sleep(1)
    b: Build = q.get_build()
    time.sleep(1)
    it, result, _ = iterate(b.url, None, None)
    assert it == IterateDecision.FINISH
    assert result is not None
    assert result.success
