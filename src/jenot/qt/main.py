from typing import cast

from meiga import (
    Error,
    Result,
)
from PyQt5.QtGui import (
    QIcon,
)
from PyQt5.QtWidgets import (
    QMessageBox,
    QWidget,
)

from jenot import (
    logo,
    PollResult,
)
from jenot.args import Args
import jenot.notify as jnotify
from jenot.qt.processor import Processor


class MainWidget(QWidget):
    args: Args
    processors: list[Processor] = []


    def __init__(self) -> None:
        super().__init__()
        try:
            self.args = Args.parse(build_required=False)
        except SystemExit:
            QMessageBox.critical(None, 'Startup failed',
                "Could not parse some of required parameters, check your .jenotrc")
            raise
        self.jenot_icon = QIcon(logo('png'))


    def notify(self, result: Result[PollResult, Error], url: str) -> None:
        # have to store msgbox somewhere so python won't dispose of it
        self.msgbox = jnotify.qt(url, result)
        self.msgbox.show()

        if self.args.telegram:
            jnotify.telegram(url, result)


    def register(self, p: Processor) -> None:
        self.processors.append(p)
        p.finished.connect(self.notify)
        p.finished.connect(lambda: self.unregister(p))
        p.start()


    def unregister(self, p: Processor) -> None:
        self.processors.remove(p)
