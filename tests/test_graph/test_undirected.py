import pytest
from graph.undirected import Graph, DFS, BFS


@pytest.fixture
def num_vertices():
    return 5


@pytest.fixture
def edges():
    return [(0, 1),
            (0, 2),
            (0, 3),
            (1, 2),
            (2, 4),
            (3, 4)]

@pytest.fixture
def graph(num_vertices, edges):
    g = Graph(num_vertices)

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
    s = search_class(graph, source)
    return s


@pytest.mark.parametrize('search_class', [DFS, BFS])
def test_search(search, num_vertices):
    print()
    print(search.__class__.__name__)
    for v in range(num_vertices):
        path_to = [x for x in search.path(v)]
        print(f'path to {v}: {path_to}')
