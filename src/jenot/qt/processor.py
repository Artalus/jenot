from meiga import Result
from PyQt5.QtCore import (
    QObject,
    QThread,
    pyqtSignal,
)

from jenot import run_poll

class Processor(QObject):
    # PyQt does not understand meiga's Result[Foo, Bar], so we use simply Result here
    finished = pyqtSignal(Result, str)

    def __init__(self, jenkins_base_url: str, user: str, token: str, build_part: str):
        super().__init__()
        self.jenkins_base_url = jenkins_base_url
        self.user = user
        self.token = token
        self.build_part = build_part

        thread = QThread()
        self.moveToThread(thread)
        thread.started.connect(self._run)
        self.finished.connect(thread.quit)
        self.finished.connect(self.deleteLater)
        thread.finished.connect(thread.deleteLater)

        self._thread = thread


    def _run(self) -> None:
        results = run_poll(self.jenkins_base_url, self.user, self.token, self.build_part)
        self.finished.emit(*results)

    def start(self) -> None:
        self._thread.start()
