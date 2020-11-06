class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        left = f', l={self.left}' if self.left else ''
        right = f', r={self.right}' if self.right else ''
        return f'<{self.key}{left}{right}>'

    def put(self, node):
        ''' Insert a node '''
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
        ''' Find a node '''
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
        ''' Delete a node '''
        if key == self.key:
            if self.left is not None:
                # pick right most object from left (immediate predecessor)
                max = self.left.max()
                self.key = max.key
                self.value = max.value

                # recursively delete max from left
                if not self.left.delete(max.key):
                    self.left = None
                return True

            elif self.right is not None:
                # pick left most ojbect from right (immediate successor)
                min = self.right.min()
                self.key = min.key
                self.value = min.value

                # recursively delete min from right
                if not self.right.delete(min.key):
                    self.right = None

                return True
            else:
                # I have no children, delete me from parent
                return False

        elif key < self.key and self.left is not None:
            # look to the left
            if not self.left.delete(key):
                self.left = None
            return True

        elif key > self.key and self.right is not None:
            # look to the right
            if not self.right.delete(key):
                self.right = None
            return True

        # key not found
        raise Exception(f'Key {key} not found')

    def min(self):
        ''' Find the minimum node in this three '''
        if self.left is None:
            return self
        else:
            return self.left.min()

    def max(self):
        ''' Find the maximum node in this three '''
        if self.right is None:
            return self
        else:
            return self.right.min()


class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return repr(self.root)

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
