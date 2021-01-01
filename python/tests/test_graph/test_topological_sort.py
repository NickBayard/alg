import pytest

from graph.topo_sort import TopologicalSort

def test_topo():
    edges = [(5, 0),
             (5, 2),
             (4, 0),
             (4, 1),
             (2, 3),
             (3, 1)]
    t = TopologicalSort(6, edges=edges)
    t.sort()
    assert [v for v in t.topo()] == [5, 4, 2, 3, 1, 0]
