class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'(key={self.key}, value={self.value}, left={self.left}, right={self.right})'


    def put(self, node):
        if node.key <= self.key:
            # place to left
            if self.left is None:
                self.left = node
            else:
                self.left.put(node)
        else:
            # place to right
            if self.right is None:
                self.right = node
            else:
                self.right.put(node)

    def get(self, key):
        if self.left is not None:
            if self.left.key == key:
                return self.left
            elif key < self.key:
                return self.left.get(key)
        if self.right is not None:
            if self.right.key == key:
                return self.right
            elif key > self.key:
                return self.right.get(key)

        raise Exception(f'key {key} not found')

    def delete(self, key):
        if self.key == key:
            if self.right is not None:
                # swap with right min
                # FIXME TODO copying the min key isn't enough.  It's parent must no longer link to it.
                min = self.right.min()
                self.key = min.key
                self.value = min.value

                if self.right.key == self.key:
                    self.right = None

                temp_right = min.right
                if temp_right is not None:
                    self.put(temp_right)

                return True

            elif self.left is not None:
                # clone left
                temp = self.left
                self.left = self.left.left
                self.right = self.left.right
                self.key = self.left.key
                self.value = self.left.value
                return True
            else:
                return False # self must be deleted by parent
        elif self.left is not None and key < self.key:
            if not self.left.delete(key):
                self.left = None
            return True
        elif self.right is not None and key > self.key:
            if not self.right.delete(key):
                self.right = None
            return True

        raise Exception(f'Key {key} not found')

    def min(self):
        if self.left is None:
            return self
        else:
            return self.left.min()


class BST:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        node = Node(key, value)
        if self.root is None:
            self.root = node
        else:
            self.root.put(node)

    def get(self, key):
        if self.root is None:
            raise Exception(f'Cannot find value for key "{key}".  BST is empty.')
        else:
            self.root.get(key)

    def delete(self, key):
        if self.root is None:
            raise Exception(f'Cannot find value for key "{key}".  BST is empty.')
        elif not self.root.delete(key):
            self.root = None
