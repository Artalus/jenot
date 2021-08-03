import subprocess
import shutil


def zenity(url: str, build_ok: bool) -> None:
    result = 'finished' if build_ok else 'failed'
    key = '--info' if build_ok else '--error'

    z = shutil.which('zenity')
    if not z:
        raise RuntimeError('zenity executable not found')

    p = subprocess.Popen([
        z, key,
        '--text', f'Task {url} {result}!',
        '--title', f'Build {result}'
    ])

def telegram(url: str, build_ok: bool) -> None:
    result = 'finished' if build_ok else 'failed'

    t = shutil.which('telegram-send')
    if not t:
        raise RuntimeError('telegram-send executable not found')

    p = subprocess.Popen([
        t, f'Task {url} {result}!'
    ])
