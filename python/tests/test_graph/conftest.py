import pytest

from graph.undirected import (
    Graph,
    DFS,
    ConnectedComponent,
)
from graph.directed import DiGraph, DirectedCycle


@pytest.fixture
def num_vertices():
    return 10


@pytest.fixture
def edges():
    return [(0, 3),
            (0, 6),
            (3, 6),
            (6, 8),
            (6, 9),
            (8, 9),
            (1, 2),
            (2, 5),
            (4, 5),
            (4, 7),
            (5, 7),
            ]

@pytest.fixture
def graph_class():
    return Graph

@pytest.fixture
def graph(graph_class, num_vertices, edges):
    g = graph_class(num_vertices)

    for x, y in edges:
        assert x < num_vertices
        assert y < num_vertices
        g.add_edge(x, y)

    return g


@pytest.fixture
def search_class():
    return DFS


@pytest.fixture
def source():
    return 0


@pytest.fixture
def search(search_class, graph, source, num_vertices):
    assert source < num_vertices
    return search_class(graph, source)


@pytest.fixture
def cc(graph):
    return ConnectedComponent(graph)

@pytest.fixture
def dir_cycle(graph):
    assert isinstance(graph, DiGraph)
    return DirectedCycle(graph)
