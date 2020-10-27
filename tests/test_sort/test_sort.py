import pytest
from sort import selection, insertion
from tests.test_sort.common import validate_sorted


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                #(1000, 5000),
                                                ])
def test_selection_sort(data):
    selection.sort(data)
    validate_sorted(data)


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                #(1000, 5000),
                                                ])
def test_insertion_sort(data):
    insertion.sort(data)
    validate_sorted(data)
