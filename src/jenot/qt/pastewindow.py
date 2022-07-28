from typing import (
    Optional,
)
from urllib.parse import urlparse

from meiga import (
    Error,
    Result,
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

class NoDataError(Error): pass
class InvalidDataError(Error): pass

class PasteUrlDialog(QDialog):
    result_data: Result[str, Error]

    buttonBox: QDialogButtonBox
    textEdit: QTextEdit

    def __init__(self, parent: Optional[QWidget]):
        super().__init__(parent)
        self.result_data = Result(failure=NoDataError())
        uic('window.ui', self)
        self.buttonBox.accepted.connect(self.on_accepted)
        self.textEdit.paste()




    def on_accepted(self) -> None:
        self.result_data = Result(failure=NoDataError())
        content = self.textEdit.toPlainText().strip()
        if not uri_validator(content):
            QMessageBox.warning(self, "Validation failed", f'Invalid URL:\n  {content}')
            self.result_data = Result(failure=InvalidDataError())
            return
        self.result_data = Result(success=content)
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
