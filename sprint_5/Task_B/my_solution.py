
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
