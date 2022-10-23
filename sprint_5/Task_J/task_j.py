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


if __name__ == "__main__":
    def test():
        node1 = Node(None, None, 7)
        node2 = Node(node1, None, 8)
        node3 = Node(None, node2, 7)
        new_head = insert(node3, 9)
        assert new_head is node3
        assert new_head.left.value == 6

    test()
