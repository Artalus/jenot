from PyQt5.QtCore import Qt
from typing import (
    Optional,
)
from PyQt5.QtWidgets import (
    QGridLayout,
    QLayoutItem,
    QPushButton,
    QTextEdit,
    QWidget,
)

class Example(QWidget):

    def __init__(self, parent: Optional[QWidget]):
        super().__init__(parent, Qt.Dialog)
        self.initUI()


    def initUI(self) -> None:
        # self.setFixedSize(350, 250)
        self.setWindowTitle('Quit button')
        txt = QTextEdit(self)
        qbtn = QPushButton('Quit', self)
        qbtn.resize(qbtn.sizeHint())
        # qbtn.move(50, 50)
        qbtn.clicked.connect(lambda x: quit(txt.toPlainText()))

        self.show()

def quit(msg: str) -> None:
    print(msg)
    exit(0)

if __name__ == '__main__':
    from PyQt5.QtWidgets import (
        QApplication,
    )
    app = QApplication([])
    ex = Example(None)
    app.exec()
