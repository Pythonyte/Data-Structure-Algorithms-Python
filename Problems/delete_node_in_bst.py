def delete_node_bst(current_node, key):
    """

    :param current_node:
    :param key:
    :return:
    """
    if current_node is None:
        return current_node

    if key > current_node.value:
        current_node.right = delete_node_bst(current_node.right, key)

    elif key < current_node.value:
        current_node.left = delete_node_bst(current_node.left, key)
    
    else:
        """
        # key is current_node, that means we need to delete current node
        # Now 3 options are there:
            1. if current_node is leaf simply maake it none
            2. If current_node has only one child, get than child value to current_node and remove child
            3. If current node has both child, find inorder_successor_node, place value of it into current_node
            and delete inorder_successor_node form current node right sub tree
        """

        if current_node.is_leaf():
            current_node = None

        elif current_node.has_only_one_child():

            if current_node.left:
                current_node.value = current_node.left.value
                current_node.left = None

            elif current_node.right:
                current_node.value = current_node.right.value
                current_node.right = None

        else:
            inorder_successor_node = current_node.inorder_successor(current_node)
            current_node.value = inorder_successor_node.value
            current_node.right = delete_node_bst(current_node.right, inorder_successor_node.value)

    return current_node