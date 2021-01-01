from stack_queue.dynamic_array import Array


class LIFO(Array):
    def __init__(self, size=10):
        self.right = 0
        super().__init__(size)

    def push(self, value):
        self.set(self.right, value)
        self.right += 1
        if self.right == self.capacity:
            self.grow()

    def pop(self):
        last = self.right - 1
        if last >= 0:
            item = self.get(last)
            self.set(last, None)
            self.right = last
            return item

        return None


class FIFO(Array):
    def __init__(self, size=10):
        self.left = 0
        self.right = 0
        super().__init__(size)

    def push(self, value):
        self.set(self.right, value)
        self.right += 1
        if self.right == self.capacity:
            self.grow()

    def pop(self):
        item = self.get(self.left)
        if item is not None:
            self.left += 1
        return item
