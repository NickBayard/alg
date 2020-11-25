import pytest

from graph.scc_digraph import StronglyConnectedComponent, Digraph


def test_0():
    edges = [
            (0, 1),
            (1, 2),
            (2, 0),
            (3, 2),
            (3, 4),
            (4, 5),
            (5, 3),
            (6, 5),
            (6, 7),
            (7, 8),
            (8, 9),
            (9, 6),
            (9, 10)
            ]
    graph = Digraph(11, edges=edges)
    scc = StronglyConnectedComponent(graph)
    scc.run()
    assert len(scc.components) == 4
    assert {0, 1, 2} in scc.components
    assert {3, 4, 5} in scc.components
    assert {6, 7, 8, 9} in scc.components
    assert {10} in scc.components


