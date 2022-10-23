

def solution(root, min_node=None, max_node=None) -> bool:
    if root is None:
        return bool(1)

    if min_node is not None and root.value <= min_node.value:
        return bool(0)

    if max_node is not None and root.value >= max_node.value:
        return bool(0)

    return solution(root.left, min_node, root) and solution(root.right, root, max_node)


if __name__ == "__main__":
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

    def test():
        node1 = Node(1, None, None)
        node2 = Node(4, None, None)
        node3 = Node(3, node1, node2)
        node4 = Node(8, None, None)
        node5 = Node(5, node3, node4)

        assert solution(node5)
        node2.value = 5
        assert not solution(node5)

    test()
