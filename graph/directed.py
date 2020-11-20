from graph.undirected import Graph


class DiGraph(Graph):
    def add_edge(self, source:int, dest:int):
        if dest not in self.adj[source]:
            self.adj[source].append(dest)
            self.num_e += 1

