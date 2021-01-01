import pytest
from itertools import permutations

from binary_tree.balanced import RBT, Color

@pytest.fixture
def rbt():
    return RBT()


@pytest.mark.parametrize('unique_data', [d for d in permutations([1, 2])])
def test_balanced_2_nodes(rbt, unique_data):
    # build tree
    for key in unique_data:
        rbt.put(key)

    r = rbt.root

    assert r.key == 2
    assert r.color == Color.BLACK

    assert r.left.key == 1
    assert r.left.color == Color.RED

    assert r.right is None


@pytest.mark.parametrize('unique_data', [d for d in permutations([1, 2, 3])])
def test_balanced_3_nodes(rbt, unique_data):
    # build tree
    for key in unique_data:
        rbt.put(key)

    r = rbt.root

    assert r.key == 2
    assert r.color == Color.BLACK

    assert r.left.key == 1
    assert r.left.color == Color.BLACK

    assert r.right.key == 3
    assert r.right.color == Color.BLACK


@pytest.mark.parametrize('unique_data', [[1, 2, 3, 4]])
def test_balanced_4_nodes(rbt, unique_data):
    # build tree
    for key in unique_data:
        rbt.put(key)

    r = rbt.root

    assert r.key == 2
    assert r.color == Color.BLACK

    assert r.left.key == 1
    assert r.left.color == Color.BLACK
    assert r.left.left is None
    assert r.left.right is None

    assert r.right.key == 4
    assert r.right.color == Color.BLACK
    assert r.right.left.key == 3
    assert r.right.left.color == Color.RED
    assert r.right.right is None
