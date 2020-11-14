from enum import Enum, auto

class Color(Enum):
    BLACK = auto()
    RED = auto()


class Node:
    def __init__(self, key, value, color=Color.BLACK):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = color

    def get(key):
        if self.key == key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.get(key)
        elif key > self.key and self.right is not None:
            return self.right.get(key)
        else:
            raise Exception(f'Key {key} not found')

    def put(key, value):
        if key == self.key:
            self.value = value
        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value, Color.RED)
            else:
                self.left.put(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value, Color.RED)
            else:
                self.right.put(key, value)
            self.correct()

    def correct(self):
        if self.right is not None:
            if self.right.right is not None:
                if self.right.right.color == Color.RED:
                    self.right = self.rotateLeft(self.right)
        if self.left is not None:
            if self.left.right is not None:
                if self.left.right.color == Color.RED:
                    self.left = self.rotateLeft(self.left)

    @staticmethod
    def rotateLeft(node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        node.color = Color.RED
        temp.color = Color.BLACK
        return temp

    @staticmethod
    def rotateRight(node):
        # FIXME
        temp = node.right
        node.right = temp.left
        temp.left = node
        node.color = Color.RED
        temp.color = Color.BLACK
        return temp
