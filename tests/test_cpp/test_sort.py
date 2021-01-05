import pytest

@pytest.mark.repeat(10)
@pytest.mark.parametrize('app', ['quick'])
def test_quick_sort(result, data):
    datastr = ','.join([str(v) for v in sorted(data)])
    expected = f'{datastr},\n'
    assert result == expected


@pytest.mark.repeat(10)
@pytest.mark.parametrize('app', ['heap'])
def test_heap_sort(result, data):
    datastr = ','.join([str(v) for v in sorted(data, reverse=True)])
    expected = f'{datastr},\n'
    assert result == expected
