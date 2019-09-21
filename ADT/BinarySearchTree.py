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
        """
        Insert node in  BST
        if item is less than current node, then it will move to left subtree
            if current node is not having left, just put it there...
        Sae goes with Right side...
        :param current_node:
        :param item:
        :return:
        """
        if item <= current_node.value:
            if current_node.left:
                self._insert_node(current_node.left, item)
            else:
                current_node.left = Node(item)
        else:
            if current_node.right:
                self._insert_node(current_node.right, item)
            else:
                current_node.right = Node(item)

    def find(self, item):
        self._find_node(self.root, item)

    def _find_node(self, current_node, item):
        if current_node is None:
            return False
        if current_node.value == item:
            return True
        if item <= current_node.value:
            return self._find_node(current_node.left, item)
        else:
            return self._find_node(current_node.right, item)

    def print_bst(self, traversal_type='inorder'):
        if traversal_type == 'inorder':
            self.print_inorder(self.root)

    def print_inorder(self, current_node):
        if current_node is None:
            return False

        self.print_inorder(current_node.left)
        print(current_node.value)
        self.print_inorder(current_node.right)
