import sys
import pytest
from sort import selection, insertion, quick
from tests.common import validate_sorted


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                ])
def test_selection_sort(data):
    selection.sort(data)
    validate_sorted(data)


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                ])
def test_insertion_sort(data):
    insertion.sort(data)
    validate_sorted(data)


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                ])
def test_quick_sort(data):
    quick.sort(data, shuffle=False)
    validate_sorted(data)
