import subprocess
import shutil
from typing import Any

from jenot import logo


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


def pynotifier(url: str, build_ok: bool) -> None:
    result = 'finished' if build_ok else 'failed'
    from pynotifier import Notification
    Notification(
        title='Jenot',
        description=f'Task {url} {result}!',
        icon_path=logo('auto'),
        duration=10,
        urgency='normal'
    ).send()


def qt(url: str, build_ok: bool) -> Any:
    result = 'finished' if build_ok else 'failed'
    from PyQt5.QtWidgets import QMessageBox
    return QMessageBox(
        QMessageBox.Icon.Information,
        'Jenot',
        f'Task {url} {result}!',
    )
