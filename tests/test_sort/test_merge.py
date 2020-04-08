import pytest
import random

from sort.merge import merge_sort, merge
from tests.test_sort.common import validate_sorted

@pytest.fixture
def merged(data):
    return sorted(data)

@pytest.fixture
def unmerged(merged):
    a = []
    b = []

    toggles = [random.randint(0, 1) for _ in range(len(merged))]

    assert len(toggles) == len(merged)

    for index, item in enumerate(merged):
        if toggles[index]:
            a.append(item)
        else:
            b.append(item)

    return a, b


@pytest.mark.repeat(100)
@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                (1000, 5000)])
def test_merge(merged, unmerged):
    assert merged == merge(unmerged[0], unmerged[1])

@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                (1000, 5000)])
def test_merge_sort(data):
    new_data = merge_sort(data)
    validate_sorted(new_data)
