import pytest
import random

from pathlib import Path
from binary_tree.search import BST


@pytest.fixture
def bst():
    return BST()


@pytest.fixture(scope='session')
def all_words():
    p = Path('/usr/share/dict/american-english')
    assert p.is_file()
    with p.open() as f:
        words = f.readlines()

    return [w.strip() for w in words]


@pytest.fixture
def values(data_len, all_words):
    return random.choices(all_words, k=data_len)


@pytest.mark.repeat(10)
@pytest.mark.parametrize('data_len', [3])
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
        bst.delete(min_node.key)

        # make sure it's deleted
        with pytest.raises(Exception):
            bst.get(min_node.key)
