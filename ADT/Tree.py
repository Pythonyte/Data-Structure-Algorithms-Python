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
        return  self.left is None and self.right is None

    def __str__(self):
        left = self.left.value if self.left else 'NULL'
        right = self.right.value if self.right else 'NULL'
        return "{0}<--{1}-->{2}".format(left, self.value, right)