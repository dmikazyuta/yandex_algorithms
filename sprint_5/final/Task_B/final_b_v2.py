class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def remove_node(node, parent, root):

    if node.left is None and node.right is None:
        if parent is not None:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return root
        else:
            return None

    if node.left is None:
        new_node = node.right
        if parent is not None:
            node.right = new_node.right
            node.value = new_node.value
            return root
        else:
            return new_node

        #return parent

    if node.right is None:
        new_node = node.left
        if parent is not None:
            node.left = new_node.left
            node.value = new_node.value
            return root
        else:
            return new_node
        #return parent

    # ищем мин элемент справа

    new_parent = node
    new_node = node.right

    while new_node.left is not None:
        new_parent = new_node
        new_node = new_node.left

    if new_parent != node:
        new_parent.left = new_node.right
    else:
        new_parent.right = new_node.right

    node.value = new_node.value

    return root


def search_node_by_key(root, key):
    if root is None:
        return None

    prev_parent = None
    node = root

    while node is not None:
        parent = node
        if key > parent.value:
            node = parent.right
            prev_parent = parent
        elif key < parent.value:
            node = parent.left
            prev_parent = parent
        else:
            return remove_node(node, prev_parent, root)

    return root


def remove(root, key):
    return search_node_by_key(root, key)


if __name__ == "__main__":
    def test():

        '''
        node1 = Node(None, None, 2)
        node8 = Node(None, None, 4)
        node2 = Node(node1, node8, 3)
        node3 = Node(None, node2, 1)
        node4 = Node(None, None, 6)
        node5 = Node(node4, None, 8)
        node10 = Node(None, None, 16)
        node9 = Node(None, node10, 14)
        node8 = Node(None, node9, 12)
        node6 = Node(node5, node8, 10)
        node7 = Node(node3, node6, 5)
        '''

        '''
        node1 = Node(None, None, 4)
        node2 = Node(None, node1, 3)
        node3 = Node(None, node2, 2)
        node4 = Node(None, node3, 1)
        #new_node = remove(node4, 2)
        #print(new_node)
        '''

        '''
        node1 = Node(None, None, 2)
        node2 = Node(node1, None, 3)
        node3 = Node(None, node2, 1)
        node4 = Node(None, None, 6)
        node5 = Node(node4, None, 8)
        node6 = Node(node5, None, 10)
        '''
        node7 = Node(None, None, 5)


        new_node = remove(node7, 5)
        print(new_node)

    test()
