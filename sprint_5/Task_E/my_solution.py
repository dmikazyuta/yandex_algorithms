

def solution(root, min_node=None, max_node=None) -> bool:
    if root is None:
        return bool(1)

    if min_node is not None and root.value <= min_node.value:
        return bool(0)

    if max_node is not None and root.value >= max_node.value:
        return bool(0)

    return solution(root.left, min_node, root) and solution(root.right, root, max_node)
