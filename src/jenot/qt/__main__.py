import sys
import signal

from PyQt5.QtWidgets import (
    QApplication,
)
from PyQt5.QtGui import (
    QIcon,
)

from jenot import logo
from jenot.qt.main import MainWidget
from jenot.qt.tray import JenotTray
import jenot.log as log


def _main() -> int:
    log.trace("main")
    # to kill pyqt with ^C https://stackoverflow.com/a/5160720/5232529
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    w = MainWidget()
    trayIcon = JenotTray(QIcon(logo('png')), w)

    trayIcon.show()
    return app.exec()

def main() -> int:
    try:
        return _main()
    except Exception as e:
        log.exception("exce")
        return -1


if __name__ == '__main__':
    sys.exit(main())
