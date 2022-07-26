from typing import cast
from urllib.parse import urlparse

from meiga import Result, Error

def validate_jenkins_base(jenkins_base: str) -> Result[str, Error]:
    base = urlparse(jenkins_base)
    if not base.scheme:
        return Result(failure=Error('jenkins base should have scheme'))
    if not base.netloc:
        return Result(failure=Error('jenkins base should have domain'))
    return Result(success=jenkins_base)


def normalize_build_url(url: str, jenkins_base: str) -> Result[str, Error]:
    parsed = urlparse(url)
    if parsed.scheme:
        # got full http://other.jenkins/x, possibly on different domain than `jenkins_base``
        url = parsed.geturl()
    else:
        validation = validate_jenkins_base(jenkins_base)
        if validation.is_failure:
            return validation
        base = cast(str, validation.unwrap())

        if not base.endswith('/'):
            base += '/'
        url = base + url
        # TODO: strip all suffixes with regexp or something...
        # or make sure that jenkins can handle build/1337/junit/api/json and drop this altogether
    url = (url
        .rstrip('/consoleFull')
        .rstrip('/console')
        .rstrip('/')
    )
    return Result(success=url)
