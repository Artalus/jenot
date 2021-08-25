from urllib.parse import urlparse

from typing import (
    Optional,
)
from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QMessageBox,
    QTextEdit,
    QWidget,
)

from jenot.qt import uic


def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False


class PasteUrlDialog(QDialog):
    result_data: Optional[str]

    buttonBox: QDialogButtonBox
    textEdit: QTextEdit

    def __init__(self, parent: Optional[QWidget]):
        super().__init__(parent)
        self.initUI()
        self.result_data = None
        self.textEdit.paste()


    def initUI(self) -> None:
        uic('window.ui', self)
        self.buttonBox.accepted.connect(self.on_accepted)


    def on_accepted(self) -> None:
        content = self.textEdit.toPlainText().strip()
        if not uri_validator(content):
            QMessageBox.warning(self, "Validation failed", f'Invalid URL:\n  {content}')
            return
        self.result_data = content
        self.accept()


if __name__ == '__main__':
    from PyQt5.QtWidgets import (
        QApplication,
    )
    import signal
    app = QApplication([])
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    ex = PasteUrlDialog(None)
    ex.show()
    app.exec()
