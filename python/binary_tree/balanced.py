from enum import Enum


class Color(Enum):
    BLACK = 'black'
    RED = 'red'


def correct(node):
    if node.right is not None and node.right.color == Color.RED:
        node = rotateLeft(node)
    if node.left is not None and node.left.color == Color.RED and \
        node.left.left is not None and node.left.left.color == Color.RED:
        node = rotateRight(node)
    if node.right is not None and node.right.color == Color.RED and \
        node.left is not None and node.left.color == Color.RED:
        flipColors(node)

    return node


def rotateLeft(node):
    temp = node.right
    node.right = temp.left
    temp.left = node
    temp.color = node.color
    node.color = Color.RED
    return temp


def rotateRight(node):
    temp = node.left
    node.left = temp.right
    temp.right = node
    temp.color = node.color
    node.color = Color.RED
    return temp


def flipColors(node):
    node.color = Color.RED
    if node.left is not None:
        node.left.color = Color.BLACK
    if node.right is not None:
        node.right.color = Color.BLACK


class RBT:
    def __init__(self):
        self.root = None

    def get(self, key):
        if self.root is None:
            raise Exception('RBT is empty')
        else:
            return self.root.get(key)

    def put(self, key, value=None):
        if self.root is None:
            self.root = Node(key, value, color=Color.BLACK)
        else:
            self.root.put(key, value)
            self.root = correct(self.root)
            self.root.color = Color.BLACK


class Node:
    def __init__(self, key, value=None, color=Color.RED):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = color

    def __repr__(self):
        left = f'{self.left}' if self.left is not None else ''
        right = f'{self.right}' if self.right is not None else ''
        return f'<{left}({self.key}/{self.color.value}){right}>'

    def get(self, key):
        if self.key == key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.get(key)
        elif key > self.key and self.right is not None:
            return self.right.get(key)
        else:
            raise Exception(f'Key {key} not found')

    def put(self, key, value=None):
        if key == self.key:
            self.value = value
        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.put(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.put(key, value)

        if self.right is not None:
            self.right = correct(self.right)
        if self.left is not None:
            self.left = correct(self.left)
