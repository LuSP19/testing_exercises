from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('host.com', 'test') == 'host.com/test'
    assert build_url(
        'host.com', 'test', {'search': 'python'}
    ) == 'host.com/test?search=python'
