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
