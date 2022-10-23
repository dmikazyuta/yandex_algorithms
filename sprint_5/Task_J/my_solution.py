from node import Node


def insert(root, key):
    if root is None:
        return Node(None, None, key)


    parent = None
    node = root
    while node is not None:
        parent = node
        if key >= parent.value:
            node = parent.right
        else:
            node = parent.left

    if key >= parent.value:
        parent.right = Node(None, None, key)
    else:
        parent.left = Node(None, None, key)

    return root
