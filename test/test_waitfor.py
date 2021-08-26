from util.wait import wait_for_200
import requests

def test_waitfor() -> None:
    wait_for_200('http://localhost:8080/api/json')
    assert requests.get('http://localhost:8080/job/sleep/api/json').json()['_class'] == 'hudson.model.FreeStyleProject'
