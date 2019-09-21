from ADT.Tree import Node

class BinarySearchTree:
    """
    Search
    Insert
    Print In Order
    Delete
    """
    def __init__(self, root=None):
        self.root = root

    def set_root(self, val):
        self.root = Node(val)

    def insert(self, item):
        if self.root is None:
            self.set_root(item)
        else:
            self._insert_node(self.root, item)

    def _insert_node(self, current_node, item):
        if current_node.value <= item:
            if current_node.left:
                self._insert_node(current_node.left, item)
            else:
                current_node.left = Node(item)
        else:
            if current_node.right:
                self._insert_node(current_node.right, item)
            else:
                current_node.right = Node(item)




