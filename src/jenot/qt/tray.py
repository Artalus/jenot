
from typing import Optional
from PyQt5.QtWidgets import (
    QMessageBox,
    QSystemTrayIcon,
    QMenu,
)
from PyQt5.QtGui import (
    QIcon,
)

from jenot.qt import qapplication, qlogger
from jenot.qt.main import MainWidget
from jenot.qt.pastewindow import PasteUrlDialog
from jenot.qt.processor import Processor
from jenot.qt.watchlist import WatchlistWindow


class JenotTray(QSystemTrayIcon):
    main: MainWidget
    pasteDialog: Optional[PasteUrlDialog]

    def __init__(self, icon: QIcon, parent: MainWidget):
        super().__init__(icon, parent,)
        self.main = parent
        self.logs = qlogger.LogWindow(self.main)
        self.pasteDialog = None

        menu = QMenu(parent)
        a = menu.addAction("Exit")
        a.setIcon(QIcon.fromTheme('application-exit'))
        a.triggered.connect(self.on_exit)

        a = menu.addAction("Watchlist")
        a.setIcon(QIcon.fromTheme('document-new'))
        a.triggered.connect(self.on_watchlist)

        a = menu.addAction("Logs")
        a.setIcon(QIcon.fromTheme('document-print'))
        a.triggered.connect(self.on_log)

        self.setContextMenu(menu)
        self.activated.connect(self.on_click)

    def on_click(self, reason: QSystemTrayIcon.ActivationReason) -> None:
        if reason != QSystemTrayIcon.Trigger:
            return
        if self.pasteDialog:
            self.pasteDialog.activateWindow()
            return

        # TODO: why None? shouldn't it be self.main or self?
        d = PasteUrlDialog(None)
        self.pasteDialog = d
        z = d.exec()
        self.pasteDialog = None

        if not z:
            return

        url = d.result_data.unwrap()
        assert url, 'got valid string here, all validation happens in dialog'
        a = self.main.args
        p = Processor(a.url, a.user, a.token, url)
        self.main.register(p)

    def on_exit(self) -> None:
        d = QMessageBox.question(None, "Exit?", "Sure you want to exit?")
        if d == QMessageBox.Yes:
            qapplication().exit()

    def on_watchlist(self) -> None:
        self.w = WatchlistWindow(self.main)
        self.w.show()

    def on_log(self) -> None:
        self.logs.show()
        self.logs.activateWindow()
