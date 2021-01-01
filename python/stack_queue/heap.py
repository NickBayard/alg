from stack_queue.dynamic_array import Array


class Heap(Array):
    def __init__(self, size=10):
        self.bottom = 0
        super().__init__(size)

    def insert(self, value):
        self.bottom += 1
        if self.bottom == self.capacity:
            self.grow()
        self.set(self.bottom, value)
        self.swim()

    def pop_max(self):
        value = self.get(1)
        self.swap(1, self.bottom)
        self.set(self.bottom, None)
        self.bottom -= 1

        if self.bottom < (self.capacity // 2):
            self.shrink()

        self.sink()

        return value

    def swim(self, index=None):
        if index is None:
           index = self.bottom

        while index > 1:
            parent = index // 2
            if self.get(parent) >= self.get(index):
                break
            self.swap(parent, index)
            index = parent

    def sink(self, index=1):
        while index * 2 <= self.bottom:
            child = index * 2

            if child < self.bottom and self.get(child) < self.get(child+1):
                child += 1

            if self.get(child) <= self.get(index):
                break

            self.swap(index, child)
            index = child
