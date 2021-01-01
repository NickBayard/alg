import pytest

@pytest.mark.repeat(10)
@pytest.mark.parametrize('app', ['quick'])
def test_quick_sort(result, values):
    valstr = ','.join([str(v) for v in sorted(values)])
    expected = f'{valstr},\n'
    assert result == expected


@pytest.mark.repeat(10)
@pytest.mark.parametrize('app', ['heap'])
def test_heap_sort(result, values):
    valstr = ','.join([str(v) for v in sorted(values, reverse=True)])
    expected = f'{valstr},\n'
    assert result == expected
