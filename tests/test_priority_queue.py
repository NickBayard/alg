import pytest

from stack_queue.priority_queue import PriorityQueue


@pytest.fixture
def pq():
    return PriorityQueue()


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len', [10, 100])
def test_pq(pq, data, data_len):
    for index, item in enumerate(data):
        pq.insert(item)

        assert pq.get(0) is None
        assert pq.bottom == index + 1

    # import pdb; pdb.set_trace()
    for index, item in enumerate(sorted(data, reverse=True)):
        assert item == pq.pop_max()
        assert pq.bottom == data_len - index - 1
