
def solution(node) -> int:
    if node is not None:

        result = node.value

        left_result = solution(node.left)
        right_result = solution(node.right)

        if left_result is not None and left_result > result:
            result = left_result
        if right_result is not None and right_result > result:
            result = max(result, right_result)
        return result


if __name__ == "__main__":
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

    node1 = Node(9999)
    node2 = Node(1)
    node3 = Node(3, node1, node2)
    node5 = Node(10)
    node6 = Node(1500)
    node7 = Node(100, node5, node6)
    node4 = Node(2, node3, node7)

    print(solution(node4))
