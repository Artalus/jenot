import json
import time
import yaml

import requests

from jenot import log

def logg(r: requests.Response) -> None:
    c = r.status_code
    try:
        content = yaml.dump(r.json(), indent=2)
    except json.JSONDecodeError:
        content = r.content.decode()
    log.debug(f'wait_for_200, resp=={c}:\n{content}')


def wait_for_200(url: str, sleep: float=5, timeout: float=5) -> None:
    start = time.time()
    while True:
        try:
            r = requests.get(url)
            logg(r)
            if r.status_code == requests.codes.ok:
                return
        except requests.exceptions.ConnectionError:
            pass
        if time.time() > start+timeout:
            raise TimeoutError(f'{url} did not become 200 in {timeout} seconds')
        if sleep:
            time.sleep(sleep)

if __name__ == '__main__':
    import sys
    wait_for_200(sys.argv[1], timeout=300)
