import pytest

@pytest.mark.repeat(10)
@pytest.mark.parametrize('app', ['bst'])
@pytest.mark.parametrize('use_key_value', [True])
def test_bst(result, data, values):
    results = result.split('\n')
    index = 0
    for datum, value in zip(data, values):
        assert results[index] == f'{datum}: {value}->{value}'
        assert results[index+1] == f'{datum} successfully deleted'
        index += 2
