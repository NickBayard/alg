from enum import Enum, auto


class Direction(Enum):
    RIGHT = auto()
    LEFT = auto()


class Array:
    def __init__(self, size=10):
        self.capacity = size
        self.backing = [None] * self.capacity

    def set(self, index, value):
        if index >= len(self.backing):
            raise Exception(f'Index {index} too high for array of size {len(self.backing)}')

        self.backing[index] = value

    def get(self, index):
        if index >= len(self.backing):
            raise Exception(f'Index {index} too high for array of size {len(self.backing)}')

        return self.backing[index]

    def swap(self, indexa, indexb):
        assert indexa < self.capacity
        assert indexb < self.capacity

        self.backing[indexa], self.backing[indexb] = self.backing[indexb], self.backing[indexa]

    def grow(self, direction=Direction.RIGHT):
        capacity = self.capacity * 2
        backing = [None] * capacity

        for index, item in enumerate(self.backing):
            if direction == Direction.RIGHT:
                backing[index] = item
            elif direction == Direction.LEFT:
                backing[index+self.capacity] = item

        self.capacity = capacity
        self.backing = backing

    def shrink(self, direction=Direction.RIGHT):
        capacity = self.capacity // 2
        backing = [None] * capacity

        if direction == Direction.RIGHT:
            slice = self.backing[:capacity]
        elif direction == Direction.LEFT:
            slice = self.backing[capacity:]

        for index, item in enumerate(slice):
            backing[index] = item

        self.capacity = capacity
        self.backing = backing
