import logging

from PyQt5.QtWidgets import (
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)

import jenot.log
from jenot.qt.main import MainWidget


class TextEditHandler(logging.Handler):
    def __init__(self, textEdit: QPlainTextEdit):
        super().__init__()
        self.textEdit = textEdit

    def emit(self, record: logging.LogRecord):
        msg = self.format(record)
        self.textEdit.appendPlainText(msg)


class LogWindow(QWidget):
    def __init__(self, main: MainWidget):
        super().__init__()
        self.main = main
        self.initUi()
        jenot.log.error('qt log window initialized')

    def initUi(self) -> None:
        self.textEdit = QPlainTextEdit(self)
        self.textEdit.setReadOnly(True)

        handler = TextEditHandler(self.textEdit)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        jenot.log._logger.addHandler(handler)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        self.setLayout(layout)

        self.setWindowIcon(self.main.jenot_icon)
        self.setWindowIconText("Jenot logs")
