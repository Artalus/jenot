from jenot import normalize_build_url

def test__normalize_build_url() -> None:
    JENKINS = 'http://jenkins'
    BUILD = 'job/kek/123'
    assert normalize_build_url(f'{BUILD}', JENKINS) == f'{JENKINS}/{BUILD}'
    assert normalize_build_url(f'{BUILD}/consoleFull', JENKINS) == f'{JENKINS}/{BUILD}'
    assert normalize_build_url(f'{BUILD}/console', JENKINS) == f'{JENKINS}/{BUILD}'
    assert normalize_build_url(f'{JENKINS}/{BUILD}/console', JENKINS) == f'{JENKINS}/{BUILD}'
    assert normalize_build_url(f'{JENKINS}/{BUILD}', JENKINS) == f'{JENKINS}/{BUILD}'
