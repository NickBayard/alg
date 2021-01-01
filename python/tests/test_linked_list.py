import pytest

from stack_queue.linked_list import Stack, FIFO


@pytest.fixture
def stack():
    return Stack()


@pytest.fixture
def fifo():
    return FIFO()


def test_stack(stack, data):
    assert stack.top is None

    for item in data:
        stack.push(item)

    # validate that items pop off in reversed order
    for item in reversed(data):
        assert stack.pop() == item

    assert stack.top is None
    assert stack.pop() is None


def test_fifo(fifo, data):
    for item in data:
        fifo.push(item)

    for item in data:
        assert fifo.pop() == item
