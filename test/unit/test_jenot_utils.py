import pytest

from jenot.url import normalize_build_url

@pytest.mark.parametrize('host', ['http://jenkins.local'])
@pytest.mark.parametrize('port', ['', ':8080'])
@pytest.mark.parametrize('prefix', ['', '/jenkins'])
def test__normalize_build_url__concat(host: str, port: str, prefix: str) -> None:
    JENKINS = f'{host}{port}{prefix}'
    BUILD = 'job/kek/123'
    RESULT = f'{JENKINS}/{BUILD}'
    assert normalize_build_url(f'{BUILD}', JENKINS).unwrap() == RESULT
    assert normalize_build_url(f'{BUILD}/', JENKINS).unwrap() == RESULT
    assert normalize_build_url(f'{BUILD}/console', JENKINS).unwrap() == RESULT


@pytest.mark.parametrize('host', ['http://jenkins.local'])
@pytest.mark.parametrize('port', ['', ':8080'])
@pytest.mark.parametrize('prefix', ['', '/jenkins'])
def test__normalize_build_url__same_domain(host: str, port: str, prefix: str) -> None:
    JENKINS = f'{host}{port}{prefix}'
    BUILD = 'job/kek/123'
    RESULT = f'{JENKINS}/{BUILD}'
    assert normalize_build_url(f'{JENKINS}/{BUILD}', JENKINS).unwrap() == RESULT
    assert normalize_build_url(f'{JENKINS}/{BUILD}/', JENKINS).unwrap() == RESULT
    assert normalize_build_url(f'{JENKINS}/{BUILD}/console', JENKINS).unwrap() == RESULT


@pytest.mark.parametrize('host', ['http://jenkins.local'])
@pytest.mark.parametrize('port', ['', ':8080'])
@pytest.mark.parametrize('prefix', ['', '/jenkins'])
@pytest.mark.parametrize('other_host', ['http://company'])
@pytest.mark.parametrize('other_port', ['', ':8081'])
@pytest.mark.parametrize('other_prefix', ['', '/other'])
def test__normalize_build_url__different_domain(host: str, port: str, prefix: str, other_host: str, other_port: str, other_prefix: str) -> None:
    JENKINS = f'{host}{port}{prefix}'
    OTHER = f'{other_host}{other_port}{other_prefix}'
    BUILD = 'job/kek/123'
    RESULT = f'{OTHER}/{BUILD}'
    assert normalize_build_url(f'{OTHER}/{BUILD}', JENKINS).unwrap() == RESULT
    assert normalize_build_url(f'{OTHER}/{BUILD}/', JENKINS).unwrap() == RESULT
    assert normalize_build_url(f'{OTHER}/{BUILD}/console', JENKINS).unwrap() == RESULT
