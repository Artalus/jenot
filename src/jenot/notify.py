import subprocess
import shutil
from typing import Any, cast

from meiga import (
    Error,
    Result,
)

from jenot import (
    logo,
    PollResult,
)


def zenity(url: str, result: Result[PollResult, Error]) -> None:
    msg = _result_to_message(url, result)
    key = '--info' if result.is_success and cast(PollResult, result.unwrap()).success else '--error'

    z = shutil.which('zenity')
    if not z:
        raise RuntimeError('zenity executable not found')

    p = subprocess.Popen([
        z, key,
        '--text', f'Task {url} {msg}!',
        '--title', f'Build {msg}'
    ])


def telegram(url: str, result: Result[PollResult, Error]) -> None:
    t = shutil.which('telegram-send')
    if not t:
        raise RuntimeError('telegram-send executable not found')

    p = subprocess.Popen([
        t, _result_to_message(url, result)
    ])


def pynotifier(url: str, result: Result[PollResult, Error]) -> None:
    msg = _result_to_message(url, result)
    from pynotifier import Notification
    Notification(
        title='Jenot',
        description=f'Task {url} {msg}!',
        icon_path=logo('auto'),
        duration=10,
        urgency='normal'
    ).send()


def qt(url: str, result: Result[PollResult, Error]) -> Any:
    from PyQt5.QtWidgets import QMessageBox
    return QMessageBox(
        QMessageBox.Icon.Information,
        'Jenot',
        _result_to_message(url, result),
    )

def _result_to_message(url: str, result: Result[PollResult, Error]) -> str:
    if result.is_failure:
        msg = f'Got error while polling for {url}.\nSee logs.'
    else:
        value = cast(PollResult, result.unwrap()).result
        if value == 'SUCCESS':
            outcome = 'succeeded VV'
        elif value == 'FAILURE':
            outcome = 'failed XX'
        elif value == 'ABORTED':
            outcome = 'aborted OO'
        elif value == 'UNSTABLE':
            outcome = 'is unstable !!'
        elif value == 'NOT_BUILT':
            outcome = 'not built ??'
        else:
            outcome = value
        msg = f'Task {url} :\n{outcome}!'
    return msg
