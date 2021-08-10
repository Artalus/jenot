import sys
import signal

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
)
from PyQt5.QtGui import (
    QIcon,
)

from jenot.qt.tray import JenotTray



def main() -> None:
    # to kill pyqt with ^C https://stackoverflow.com/a/5160720/5232529
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    w = QWidget()
    trayIcon = JenotTray(QIcon("logo.png"), w)

    trayIcon.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
