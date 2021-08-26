import time
import requests

def wait_for_200(url: str, sleep: float=5, timeout: float=300) -> None:
    start = time.time()
    while True:
        try:
            r = requests.get(url)
            print(r.status_code)
            print(r.content.decode())
            if r.status_code == requests.codes.ok:
                return
        except requests.exceptions.ConnectionError:
            pass
        if time.time() > start+timeout:
            raise TimeoutError(f'{url} did not become 200 in {timeout} seconds')
        time.sleep(sleep)

if __name__ == '__main__':
    import sys
    wait_for_200(sys.argv[1])
