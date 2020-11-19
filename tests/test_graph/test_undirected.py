import pytest

from graph.undirected import (
    DFS,
    BFS,
)


@pytest.mark.parametrize('search_class', [DFS, BFS])
def test_search(search, num_vertices):
    print()
    print(search.__class__.__name__)
    for v in range(num_vertices):
        path_to = [x for x in search.path(v)]
        print(f'path to {v}: {path_to}')


@pytest.mark.parametrize('num_vertices', [10])
@pytest.mark.parametrize('edges', [[(0, 3),
                                    (0, 6),
                                    (3, 6),
                                    (6, 9),
                                    (6, 8),
                                    (8, 9),
                                    (1, 2),
                                    (2, 5),
                                    (4, 5),
                                    (4, 7),
                                    (5, 7),
                                    ]])
def test_connected(cc):
    assert cc.count == 2

    assert {v for v in cc.component_vertices(0)} == {0, 3, 6, 8, 9}
    assert {v for v in cc.component_vertices(1)} == {1, 2, 4, 5, 7}
