class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


node1 = Node(1)
node2 = Node(-5)
node3 = Node(3, node1, node2)
node4 = Node(2, node3, None)

"""
10
0 0 1 2
1 2 3 None
2 2 None 4
3 3 5 6
4 3 7 8
5 0 None None
6 0 None None
7 111 None None
8 0 None 9
9 111 None None
"""


def find_max_node(node: Node):
    if node is not None:
        result = node.value
        left_result = find_max_node(node.left)
        right_result = find_max_node(node.right)\

        if left_result > result:
            result = left_result
        if right_result > result:
            result = right_result

        return result


    return max(a, b)


print(find_max_node(node4))
