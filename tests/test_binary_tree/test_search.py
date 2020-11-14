import pytest

from binary_tree.search import BST


@pytest.fixture
def bst():
    return BST()


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len', [10])
def test_bst(bst, unique_data, values):
    assert bst.root is None

    # build tree
    for key, value in zip(unique_data, values):
        bst.put(key, value)

    # import pdb; pdb.set_trace()

    for key, value in sorted(zip(unique_data, values)):
        min_node = bst.root.min()
        assert key == min_node.key
        assert value == min_node.value
        bst.delete(key)

        # make sure it's deleted
        with pytest.raises(Exception):
            bst.get(key)
