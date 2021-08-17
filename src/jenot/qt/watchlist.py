from PyQt5.QtCore import (
    Qt,
)
from PyQt5.QtGui import (
    QStandardItem,
    QStandardItemModel,
)
from PyQt5.QtWidgets import (
    QListView,
    QVBoxLayout,
    QWidget,
)

from jenot.qt import uic
from jenot.qt.main import MainWidget

class WatchlistWindow(QWidget):
    verticalLayout: QVBoxLayout
    listView: QListView
    model: QStandardItemModel

    def __init__(self, main: MainWidget):
        super().__init__()
        self.initUI()

        self.fill(main)

        # TODO: make window fit contents somehow
        # self.adjustSize()


    def initUI(self) -> None:
        uic('watchlist.ui', self)
        self.setLayout(self.verticalLayout)
        self.setWindowFlag(Qt.Drawer, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)


    def fill(self, main: MainWidget) -> None:
        self.model = QStandardItemModel(self)
        self.listView.setModel(self.model)

        for p in main.processors:
            i = QStandardItem(p.build_part)
            self.model.appendRow([i])


if __name__ == '__main__':
    from PyQt5.QtWidgets import (
        QApplication,
    )
    import random
    class ProcessorStub:
        def __init__(self) -> None:
            r = random.randrange(5,10)
            self.build_part = r * str(id(self))
    class MainStub:
        processors = [ProcessorStub(), ProcessorStub(), ProcessorStub()]
    app = QApplication([])
    app.setQuitOnLastWindowClosed(True)
    m = MainStub()
    ex = WatchlistWindow(m)
    ex.show()
    app.exec()
