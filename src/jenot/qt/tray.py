
from PyQt5.QtWidgets import (
    QSystemTrayIcon,
    QMenu,
)
from PyQt5.QtGui import (
    QIcon,
)

from jenot.qt import qapplication
from jenot.qt.main import MainWidget
from jenot.qt.pastewindow import PasteUrlDialog
from jenot.qt.processor import Processor
from jenot.qt.watchlist import WatchlistWindow


class JenotTray(QSystemTrayIcon):
    main: MainWidget

    def __init__(self, icon: QIcon, parent: MainWidget):
        super().__init__(icon, parent,)
        self.main = parent

        menu = QMenu(parent)
        a = menu.addAction("Exit")
        a.setIcon(QIcon.fromTheme('application-exit'))
        a.triggered.connect(qapplication().quit)

        a = menu.addAction("Watchlist")
        a.setIcon(QIcon.fromTheme('document-new'))
        a.triggered.connect(self.on_watchlist)

        self.setContextMenu(menu)
        self.activated.connect(self.on_click)

    def on_click(self, reason: QSystemTrayIcon.ActivationReason) -> None:
        d = PasteUrlDialog(None)
        z = d.exec()
        if not z:
            return
        assert d.result_data
        a = self.main.args
        p = Processor(a.url, a.user, a.token, d.result_data)
        self.main.register(p)

    def on_watchlist(self) -> None:
        self.w = WatchlistWindow(self.main)
        self.w.show()
