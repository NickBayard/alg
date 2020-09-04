import pytest
from sort.selection import selection_sort
from tests.test_sort.common import validate_sorted


@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                (1000, 5000)])
def test_selection_sort(data):
    new_data = selection_sort(data)
    validate_sorted(new_data)
