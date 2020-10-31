from enum import Enum, auto


class Grow(Enum):
    RIGHT = auto()
    LEFT = auto()


class Array:
    def __init__(self, size=10):
        self.right = 0
        self.capacity = size
        self.backing = [None] * self.capacity

    def set(self, index, value):
        self.backing[index] = value

    def get(self, index):
        return self.backing[index]

    def grow(self, direction):
        capacity = self.capacity * 2
        backing = [None] * capacity

        for index, item in enumerate(self.backing):
            if direction == Grow.RIGHT:
                backing[index] = item
            elif direction == Grow.LEFT:
                backing[index+self.capacity] = item

        self.capacity = capacity
        self.backing = backing


class Stack(Array):
    def __init__(self, size=10):
        self.right = 0
        super().__init__(size)

    def push(self, value):
        self.set(self.right, value)
        self.right += 1
        if self.right == self.capacity:
            self.grow(Grow.RIGHT)

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
            self.grow(Grow.RIGHT)

    def pop(self):
        item = self.get(self.left)
        if item is not None:
            self.left += 1
        return item
