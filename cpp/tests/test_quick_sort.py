import pytest

@pytest.mark.repeat(10)
def test_0(result, values):
    valstr = ','.join([str(v) for v in sorted(values)])
    expected = f'{valstr},\n'
    assert result == expected
