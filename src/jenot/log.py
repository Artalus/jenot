import logging
from typing import Any
from systemd.journal import JournaldLogHandler

_logger = logging.getLogger('jenot')
_logger.addHandler(JournaldLogHandler())
_logger.setLevel(logging.DEBUG)
_logger.info("jenot log initialized")

debuf = _logger.debug
info = _logger.info
error = _logger.error
exception = _logger.exception
warning = _logger.warning
setLevel = _logger.setLevel

def trace(*x: Any, **xx: Any) -> None:
    _logger.debug(*x, **xx)
