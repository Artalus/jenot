import sys
import signal
import traceback
from typing import Any, Type

from PyQt5.QtWidgets import (
    QApplication,
)

from jenot.qt.main import MainWidget
from jenot.qt.tray import JenotTray
import jenot.log as log


def exception_hook(exc_type: Type[BaseException], exc_value: BaseException, exc_tb: Any) -> None:
    # TODO: prints `NoneType: None` at the end of trace for some reason
    tb = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
    log.exception(f'unhandled exception:\n{tb}')
    QApplication.exit(-1)


def main() -> int:
    sys.excepthook = exception_hook
    log.trace(f'{sys.argv[0]} starting')
    # to kill pyqt with ^C https://stackoverflow.com/a/5160720/5232529
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    w = MainWidget()
    trayIcon = JenotTray(w.jenot_icon, w)

    trayIcon.show()
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
