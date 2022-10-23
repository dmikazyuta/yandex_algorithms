
def find_max_depth(root):
    if root is None:
        return 0
    return max(find_max_depth(root.left), find_max_depth(root.right)) + 1


def solution(root) -> bool:
    if root is None:
        return bool(1)

    left = find_max_depth(root.left)
    right = find_max_depth(root.right)

    if abs(left - right) <= 1:
        return solution(root.left) and solution(root.right)
    else:
        return bool(0)


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

        print(solution(node5))

    test()
