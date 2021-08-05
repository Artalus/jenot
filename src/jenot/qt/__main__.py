import sys
import signal

from PyQt5.QtWidgets import (
    QApplication,
    QSystemTrayIcon,
    QMenu,
    QWidget,
)
from PyQt5.QtGui import (
    QIcon,
)

from jenot.qt import qapplication


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon: QIcon, parent: QWidget):
        super().__init__(icon, parent)
        menu = QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.setIcon(QIcon.fromTheme('application-exit'))
        exitAction.triggered.connect(qapplication().quit)
        self.setContextMenu(menu)
        self.activated.connect(lambda x: self.showMessage("hello", "world"))


def main() -> None:
    # to kill pyqt with ^C https://stackoverflow.com/a/5160720/5232529
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)

    w = QWidget()
    trayIcon = SystemTrayIcon(QIcon("logo.png"), w)

    trayIcon.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
