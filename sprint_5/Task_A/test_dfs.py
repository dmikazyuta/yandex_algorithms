
def print_nodes(root, result):
    if root is not None:
        print_nodes(root.left, result)
        print_nodes(root.right, result)

        result.append(root.value)


if __name__ == "__main__":
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

    def test():
        node1 = Node(4)
        node2 = Node(1, node1)
        node3 = Node(5)
        node4 = Node(2)
        node5 = Node(6, node3, node4)
        node6 = Node(3, node2, node5)

        result = []
        print_nodes(node6, result)
        print(*result)

    test()
