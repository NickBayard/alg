import pytest

from stack_queue.heap import Heap
from tests.common import validate_sorted


@pytest.fixture
def heap():
    return Heap()


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len', [10, 100])
def test_heap(heap, data, data_len):
    for index, item in enumerate(data):
        heap.insert(item)

        assert heap.get(0) is None
        assert heap.bottom == index + 1

    # import pdb; pdb.set_trace()
    for index, item in enumerate(sorted(data, reverse=True)):
        assert item == heap.pop_max()
        assert heap.bottom == data_len - index - 1


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len, data_max', [(10, 100),
                                                (100, 500),
                                                ])
def test_heap_sort(heap, data):
    for item in data:
        heap.insert(item)

    for index in range(len(data)):
        data[index] = heap.pop_max()

    data = data[::-1]
    validate_sorted(data)
