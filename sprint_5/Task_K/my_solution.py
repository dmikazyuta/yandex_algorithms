def print_range(node, l, r):
    if node is None:
        return

    if node.value > r:
        print_range(node.left, l, r)
    elif node.value < l:
        print_range(node.right, l, r)
    else:
        print_range(node.left, l, r)
        print(node.value, end=' ')
        print_range(node.right, l, r)