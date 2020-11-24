import pytest

from graph.undirected import (
    Graph,
    DFS,
    BFS,
)
from graph.directed import DiGraph, DirectedCycle



@pytest.mark.parametrize('graph_class', [Graph, DiGraph])
@pytest.mark.parametrize('search_class', [DFS, BFS])
def test_search(search):
    for vertex in [1, 2, 4, 5, 7]:
        assert not search.has_path(vertex)

    for vertex in [3, 6, 8, 9]:
        assert search.has_path(vertex)


@pytest.mark.parametrize('graph_class', [Graph, DiGraph])
@pytest.mark.parametrize('search_class', [BFS])
def test_shortest_path(search):
    for vertex in [1, 2, 4, 5, 7]:
        assert not search.has_path(vertex)

    for vertex in [3, 6, 8, 9]:
        assert search.has_path(vertex)

    assert [v for v in search.path(3)] == [0, 3]
    assert [v for v in search.path(6)] == [0, 6]
    assert [v for v in search.path(8)] == [0, 6, 8]
    assert [v for v in search.path(9)] == [0, 6, 9]


def test_connected_undirected(cc, graph_class):
    assert cc.count == 2

    assert {v for v in cc.component_vertices(0)} == {0, 3, 6, 8, 9}
    assert {v for v in cc.component_vertices(1)} == {1, 2, 4, 5, 7}


@pytest.mark.parametrize('num_vertices', [6])
@pytest.mark.parametrize('edges', [[(0, 1),
                                    (1, 2),
                                    (2, 3),
                                    (3, 4),
                                    (4, 2),
                                    (3, 5),
                                    ]])
@pytest.mark.parametrize('graph_class', [DiGraph])
def test_directed_cycle(dir_cycle):
    dir_cycle.search()
    print([x for x in dir_cylce.get()])
