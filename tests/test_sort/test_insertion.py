import pytest
from sort.insertion import insertion_sort
from tests.test_sort.common import validate_sorted


@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                (1000, 5000)])
def test_insertion_sort(data):
    new_data = insertion_sort(data)
    validate_sorted(new_data)
