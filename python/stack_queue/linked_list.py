class Node:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value, previous=self.top)
        self.top = node

    def pop(self):
        node = self.top
        if node is not None:
            self.top = node.previous
            return node.value
        else:
            return node


class FIFO:
    def __init__(self):
        self.front = None
        self.back = None

    def push(self, value):
        node = Node(value)
        if self.back is None:
            self.back = node
            self.front = node
        else:
            node.previous = self.back
            node.previous.next = node
            self.back = node

    def pop(self):
        if self.front is not None:
            node = self.front
            self.front = node.next
            return node.value
        else:
            return None
