from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QDialogButtonBox as BB,
    QMessageBox,
)
from pytestqt.qtbot import QtBot
import pytest

from jenot.qt.pastewindow import (
    InvalidDataError,
    NoDataError,
    PasteUrlDialog,
)

LMB = Qt.MouseButton.LeftButton


def test_cancel(qtbot: QtBot) -> None:
    d = PasteUrlDialog(None)
    qtbot.addWidget(d)

    assert isinstance(d.result_data.value, NoDataError)

    qtbot.mouseClick(d.buttonBox.button(BB.StandardButton.Cancel), LMB)
    assert isinstance(d.result_data.value, NoDataError)


@pytest.mark.parametrize('url', ['http://jenkins/job/somejob/1', 'http://jenkins/job/somejob/1/console', 'http://jenkins/job/somejob/1/consoleFull'])
def test_accept_valid_url(qtbot: QtBot, url: str) -> None:
    # clear qt clipboard in case it contains something when pytest runs
    QApplication.clipboard().clear()
    d = PasteUrlDialog(None)
    qtbot.addWidget(d)

    assert d.result_data.is_failure
    assert isinstance(d.result_data.value, NoDataError)

    qtbot.keyClicks(d.textEdit, url)
    qtbot.mouseClick(d.buttonBox.button(BB.StandardButton.Ok), LMB)

    assert d.result_data.is_success
    assert isinstance(d.result_data.value, str)
    assert d.result_data.unwrap() == url


def test_accept_clipboard(qtbot: QtBot) -> None:
    url = 'http://jenkins/job/somejob/1'
    QApplication.clipboard().setText(url)
    d = PasteUrlDialog(None)
    qtbot.addWidget(d)

    assert d.result_data.is_failure
    assert isinstance(d.result_data.value, NoDataError)

    qtbot.mouseClick(d.buttonBox.button(BB.StandardButton.Ok), LMB)

    assert d.result_data.is_success
    assert isinstance(d.result_data.value, str)
    assert d.result_data.unwrap() == url
    # without it test freezes at exit for some time and then says
    #    QXcbClipboard: Unable to receive an event from the clipboard manager in a reasonable time
    QApplication.clipboard().clear()


@pytest.mark.parametrize(
    'url', [
        '',
        'abrakadabra',
        pytest.param('http://jenkins/1\nhttp://jenkins/2', marks=pytest.mark.xfail(reason='no multiline support'))
    ],
)
def test_invalid_data(qtbot: QtBot, url: str, monkeypatch: pytest.MonkeyPatch) -> None:
    QApplication.clipboard().setText(url)
    d = PasteUrlDialog(None)
    qtbot.addWidget(d)

    assert d.result_data.is_failure
    assert isinstance(d.result_data.value, NoDataError)

    monkeypatch.setattr(
        QMessageBox, 'warning', classmethod(lambda *a, **kw: None)
    )
    qtbot.mouseClick(d.buttonBox.button(BB.StandardButton.Ok), LMB)

    assert d.result_data.is_failure
    assert isinstance(d.result_data.value, InvalidDataError)
    # see above
    QApplication.clipboard().clear()
