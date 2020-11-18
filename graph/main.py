from graph.undirected import Graph, DFS
from pathlib import Path


path = Path('graph/graph.txt')

first = True

edges = []
with path.open() as f:
    for line in f:
        if first:
            num = int(line.strip())
            first = False
        else:
            edges.append(tuple(int(v) for v in line.strip().split(' ')))

g = Graph(num)
for v, w in edges:
    g.add_edge(v, w)

search = DFS(g, 0)

# print(search.edge_to)

for v in range(g.num_v):
    path_to = [x for x in search.path(v)]
    print(f'path to {v}: {path_to}')
