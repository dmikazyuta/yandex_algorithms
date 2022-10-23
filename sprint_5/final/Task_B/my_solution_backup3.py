def search_node_by_key(root, key):
    if root is None:
        return None

    prev_parent = None
    node = root

    while node is not None:
        parent = node
        if key > parent.value:
            node = parent.right
            prev_parent = parent
        elif key < parent.value:
            node = parent.left
            prev_parent = parent
        else:
            return get_new_root(node, prev_parent, root)

    return root


def search_max_node_from_left(root):
    node = root.left
    parent = root
    while node.right is not None:
        parent = node
        node = node.right

    #node.right = parent.right

    #if node.left is None:
    #    parent.left = None

    if parent.right == node:
        parent.right = None

    return node


def search_min_node_from_right(root):
    node = root.right
    parent = root
    while node.left is not None:
        parent = node
        node = node.left

    parent.left = None
    #node.right = parent.right

    return node


def get_new_root(node, parent, root):
    #node_list = search_node_by_key(root, key)

    key = node.value

    # parents exists
    if parent is not None:

        if node.left is None and node.right is None:
            if parent.value <= key:
                parent.right = None
            elif parent.value >= key:
                parent.left = None

        elif node.left is not None:
            max_node_from_left = search_max_node_from_left(node)
            max_node_from_left.right = node.right
            #max_node_from_left.left = node.left

            if parent.value <= key:
                parent.right = max_node_from_left
            elif parent.value >= key:
                parent.left = max_node_from_left

        elif node.right is not None:
            min_node_from_right = search_min_node_from_right(node)
            if node.right == min_node_from_right:
                min_node_from_right.right = None
            else:
                min_node_from_right.right = node.right

            if parent.value <= key:
                parent.right = min_node_from_right
            elif parent.value >= key:
                parent.left = min_node_from_right

    # no parents
    else:
        if node.left is not None:
            max_node_from_left = search_max_node_from_left(node)
            max_node_from_left.left = node.left
            max_node_from_left.right = node.right
            root = max_node_from_left
        elif node.right is not None:
            min_node_from_right = search_min_node_from_right(node)
            if node.right == min_node_from_right:
                min_node_from_right.right = None
            else:
                min_node_from_right.right = node.right
            min_node_from_right.left = node.left
            root = min_node_from_right
        else:
            root = None
    #print(root)
    return root


def remove(root, key):
    return search_node_by_key(root, key)