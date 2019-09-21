class Node:
    """
    set a value in node
    get value of node
    get children of a node
    """
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get(self):
        return self.value

    def set(self, value=None):
        self.value = value

    def get_children(self):
        children = []
        children.extend([self.left, self.right])
        return children

    def is_leaf(self):
        return self.left is None and self.right is None

    def has_only_one_child(self):
        if self.left is not None and self.right is not None:
            return False
        elif self.left is None and self.right is None:
            return False
        return True

    def inorder_successor(self, current_node):
        """
        for a node, inorder_successor is just next element..
        which will lie in left most side of node's right chlid
        :return:
        """
        if not current_node.right:
            return None
        inorder_successor_node = current_node.right
        while inorder_successor_node.left:
            inorder_successor_node = inorder_successor_node.left
        return inorder_successor_node

    def inorder_predecessor(self, current_node):
        """
        for a node, inorder_successor is just prev element..
        which will lie in right most side of node's left chlid
        :return:
        """
        if not current_node.left:
            return None
        inorder_successor_node = current_node.left
        while inorder_successor_node.right:
            inorder_successor_node = inorder_successor_node.right
        return inorder_successor_node

    def __str__(self):
        left = self.left.value if self.left else 'NULL'
        right = self.right.value if self.right else 'NULL'
        return "{0}<--{1}-->{2}".format(left, self.value, right)