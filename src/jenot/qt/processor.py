import time

from PyQt5.QtCore import (
    QObject,
    QThread,
    pyqtSignal,
)

from jenot import run
from jenot import log

class Processor(QObject):
    finished = pyqtSignal(int, str)

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
        for attempt in range(1,1+3):
            try:
                result = run(self.jenkins_base_url, self.user, self.token, self.build_part)
                self.finished.emit(*result)
                return
            except Exception as e:
                log.exception(f'Watch attempt {attempt}, exception happened: {e}')
                log.info('sleeping for 5 sec before retry...')
                time.sleep(5)
        else:
            log.error('Watch failed after 3 attempts')
            self.finished.emit(1, self.build_part)

    def start(self) -> None:
        self._thread.start()
