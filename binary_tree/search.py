class Node:
    def __init__(self, key, value, size=1):
        self.key = key
        self.value = value
        self.size = size
        self.left = None
        self.right = None

    def put(self, node):
        if node.value <= self.value:
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
        self.size +=1

    def get(self, key):
        if self.left.key == key:
            return self.left
        elif self.right.key == key:
            return self.right
        elif key < self.key:
            return self.left.get(key)
        elif key > self.key:
            return self.right.get(key)

    def delete(self, key):
        if self.left.key == key:
            self.left = self.rebuild(self.left)
        elif self.right.key == key:
            self.right = self.rebuild(self.right)
        elif key < self.key:
            self.left.delete(key)
        elif key > self.key:
            self.right.delete(key)

    def rebuild(self, node):
        if node is node.left:
            pass
        elif node is node.right:
            pass

        if node.left is None:
            # node is the minimum.  just move up right tree
            return node.right
        # find node with left=None.  That's the minimum
        if node.left.left is None:
            replace = node.left
            right = node.left.right

        # copy the right tree of this node



class BST:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        node = Node(key, value)
        is self.root is None:
            self.root = node
        else:
            self.root.put(node)

    def get(self, key):
        if self.root is None:
            raise Exception(f'Cannot find value for key "{key}".  BST is empty.')
        else:
            self.root.get(key)
