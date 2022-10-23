
def print_nodes(root, result):
    queue = []
    if root is not None:
        queue.append(root)

    while len(queue) > 0:
        node = queue.pop()
        result.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    print(*result)


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

    test()
