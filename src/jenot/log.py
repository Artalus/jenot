import logging
from platform import system
from typing import Any

_logger = logging.getLogger('jenot')
_logger.addHandler(logging.StreamHandler())
_logger.setLevel(logging.DEBUG)

if system() == 'Linux':
    try:
        from systemd.journal import JournaldLogHandler
        _logger.addHandler(JournaldLogHandler())
    except ImportError:
        _logger.info("systemd python module not installed, no journald support")
_logger.info("jenot log initialized")

debug = _logger.debug
info = _logger.info
error = _logger.error
exception = _logger.exception
warning = _logger.warning
setLevel = _logger.setLevel

def trace(*x: Any, **xx: Any) -> None:
    _logger.debug(*x, **xx)
