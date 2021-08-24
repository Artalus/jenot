from PyQt5.QtGui import (
    QIcon,
)
from PyQt5.QtWidgets import (
    QMessageBox,
    QWidget,
)

from jenot import logo
from jenot.args import Args
import jenot.notify as jnotify
from jenot.qt.processor import Processor

class MainWidget(QWidget):
    args: Args
    processors: list[Processor] = []

    def __init__(self):
        super().__init__()
        self.args = Args.parse(build_required=False)
        try:
            self.args = Args.parse(build_required=False)
        except SystemExit:
            QMessageBox.critical(None, 'Startup failed',
                "Could not parse some of required parameters, check your .jenotrc")
            raise
        self.jenot_icon = QIcon(logo('png'))


    def notify(self, result: int, url: str) -> None:
        if self.args.zenity:
            jnotify.zenity(url, result==0)
        if self.args.telegram:
            jnotify.telegram(url, result==0)
        if self.args.pynotifier:
            jnotify.pynotifier(url, result==0)


    def register(self, p: Processor) -> None:
        self.processors.append(p)
        p.finished.connect(self.notify)
        p.finished.connect(lambda: self.unregister(p))
        p.start()


    def unregister(self, p: Processor) -> None:
        self.processors.remove(p)
