import pytest

from stack_queue.FIFO_LIFO import LIFO, FIFO


@pytest.fixture
def stack():
    return LIFO()


@pytest.fixture
def fifo():
    return FIFO()


def test_stack(stack, data):
    assert stack.right == 0

    for item in data:
        stack.push(item)

    # validate that items pop off in reversed order
    for item in reversed(data):
        assert stack.pop() == item

    assert stack.right == 0
    assert stack.pop() is None


def test_fifo(fifo, data):
    for item in data:
        fifo.push(item)

    for item in data:
        assert fifo.pop() == item
