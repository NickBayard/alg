class Digraph:
    def __init__(self, num_vertices, edges=None):
        self.num = num_vertices

        self.adjacent = []
        for _ in range(num_vertices):
            self.adjacent.append([])

        for source, dest in edges:
            self.add_edge(source, dest)

    def add_edge(self, source, dest):
        self.adjacent[source].append(dest)

    def reverse(self):
        edges = []
        for source, adjacent in enumerate(self.adjacent):
            for dest in adjacent:
                edges.append((dest, source))

        return Digraph(self.num, edges=edges)


class StronglyConnectedComponent:
    def __init__(self, graph):
        self.graph = graph
        self.marked = [False] * graph.num
        self.component_map = [None] * graph.num
        self.components = [set()]
        self.count = 0
        self.stack = []

    def run(self):
        self.build_stack()
        # reset marked
        self.marked = [False] * self.graph.num
        self.graph = self.graph.reverse()
        self.collect_components()
        self.count -= 1
        self.components.pop()

    def build_stack(self):
        for vertex in range(self.graph.num):
            if not self.marked[vertex]:
                self.marked[vertex] = True
                self.dfs_stack(vertex)
                self.stack.append(vertex)

    def dfs_stack(self, source):
        for vertex in self.graph.adjacent[source]:
            if not self.marked[vertex]:
                self.marked[vertex] = True
                self.dfs_stack(vertex)
                self.stack.append(vertex)

    def collect_components(self):
        while self.stack:
            vertex = self.stack.pop()
            if not self.marked[vertex]:
                self.component_map[vertex] = self.count
                self.components[self.count].add(vertex)
                self.marked[vertex] = True
                self.dfs_component(vertex)
                self.count += 1
                self.components.append(set())

    def dfs_component(self, source):
        for vertex in self.graph.adjacent[source]:
            if not self.marked[vertex]:
                self.component_map[vertex] = self.count
                self.components[self.count].add(vertex)
                self.marked[vertex] = True
                self.dfs_component(vertex)
