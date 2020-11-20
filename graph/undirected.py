from queue import Queue


class Graph:
    def __init__(self, num_vertices):
        self.adj = []
        for _ in range(num_vertices):
            self.adj.append([])
        self.num_v = num_vertices
        self.num_e = 0

    def add_edge(self, source: int, dest: int):
        if source >= self.num_v:
            raise Exception(f'source {source} outside index range of {self.num_v}')
        if dest >= self.num_v:
            raise Exception(f'destination {dest} outside index range of {self.num_v}')

        if dest not in self.adj[source] and source not in self.adj[dest]:
            self.adj[source].append(dest)
            self.adj[dest].append(source)
            self.num_e += 1

    def adjacent(self, vertex: int):
        if vertex >= self.num_v:
            raise Exception(f'vertex {vertex} outside index range of {self.num_v}')

        for v in self.adj[vertex]:
            yield v


class Search:
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.edge_to = [None] * graph.num_v
        self.marked = [False] * graph.num_v

    def search(self):
        raise NotImplementedError

    def has_path(self, dest: int) -> bool:
        return self.edge_to[dest] is not None

    def path(self, dest: int):
        result = []
        v = dest
        result.append(dest)

        while v != self.source:
            w = self.edge_to[v]
            result.append(w)
            v = w

        for v in result[::-1]:
            yield v


class DFS(Search):
    def __init__(self, graph, source):
        super().__init__(graph, source)
        self.search()

    def search(self):
        self.dfs(self.source)

    def dfs(self, source: int):
        if source >= self.graph.num_v:
            raise Exception(f'source {source} outside index range of {self.graph.num_v}')

        self.marked[source] = True
        for v in self.graph.adjacent(source):
            if not self.marked[v]:
                self.marked[v] = True
                if v != source:
                    self.edge_to[v] = source
                    self.dfs(v)


class BFS(Search):
    def __init__(self, graph, source):
        super().__init__(graph, source)
        self.queue = Queue()
        self.queue.put(source)
        self.marked[source] = True
        self.search()

    def search(self):
        while not self.queue.empty():
            source = self.queue.get()

            for v in self.graph.adjacent(source):
                if not self.marked[v] and v != source:
                    self.queue.put(v)
                    self.marked[v] = True
                    self.edge_to[v] = source


class ConnectedComponent:
    def __init__(self, graph):
        self.graph = graph
        self.count = 0
        self.component_index = [None] * graph.num_v  # Replaces marked
        self.search()

    def search(self):
        for source in range(self.graph.num_v):
            if self.component_index[source] is None:
                self.component_index[source] = self.count
                self.dfs(source)
                self.count += 1

    def dfs(self, source):
        for v in self.graph.adjacent(source):
            if self.component_index[v] is None and v != source:
                self.component_index[v] = self.count

                self.dfs(v)

    def is_connected(self, v: int, w: int) -> bool:
        return self.component_index[v] is not None and self.component_index[v] == self.component_index[w]

    def component_vertices(self, comp_index: int):
        for vertex, component in enumerate(self.component_index):
            if component == comp_index:
                yield vertex
