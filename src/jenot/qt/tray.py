
from PyQt5.QtWidgets import (
    QSystemTrayIcon,
    QMenu,
    QWidget,
)
from PyQt5.QtGui import (
    QIcon,
)

from jenot.qt import qapplication
from jenot.qt.pastewindow import PasteUrlDialog
from jenot.qt.processor import Processor


class JenotTray(QSystemTrayIcon):
    def __init__(self, icon: QIcon, parent: QWidget):
        super().__init__(icon, parent,)
        self.main_widget = parent
        self.setProperty

        menu = QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.setIcon(QIcon.fromTheme('application-exit'))
        exitAction.triggered.connect(qapplication().quit)
        self.setContextMenu(menu)
        self.activated.connect(self.on_click)

    def on_click(self, reason: QSystemTrayIcon.ActivationReason) -> None:
        d = PasteUrlDialog(None)
        z = d.exec()
        print(z)
        if z:
            print(d.result_data)
