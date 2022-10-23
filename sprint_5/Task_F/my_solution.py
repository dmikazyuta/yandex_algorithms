def solution(root) -> int:
    queue = []
    count = 0
    if root is None:
        return count

    queue.append([root, count + 1])
    max_count = 0
    while len(queue) > 0:
        node_lvl = queue.pop()
        node = node_lvl[0]
        count = node_lvl[1]
        if node.left is not None:
            queue.append([node.left, count + 1])
        if node.right is not None:
            queue.append([node.right, count + 1])

        max_count = max(max_count, count)

    return max_count
