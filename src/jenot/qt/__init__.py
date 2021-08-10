from pathlib import Path

import PyQt5.uic
from PyQt5.QtCore import (
    QCoreApplication,
)
from PyQt5.QtWidgets import (
    QApplication,
)

def qapplication() -> QCoreApplication:
    a = QApplication.instance()
    assert a
    return a

def uic(name: str, self: PyQt5.QtCore.QObject) -> None:
    ui = Path(__file__).parent / 'ui' / name
    PyQt5.uic.loadUi(ui, self)
