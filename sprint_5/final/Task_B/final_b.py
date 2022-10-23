# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


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
            return get_new_root(node, prev_parent, root)

    return root


def search_max_node_from_left(root):
    node = root.left
    parent = root
    while node.right is not None:
        parent = node
        node = node.right

    #node.right = parent.right

    #if node.left is None:
    #    parent.left = None

    if parent.right == node:
        parent.right = None

    return node


def search_min_node_from_right(root):
    node = root.right
    parent = root
    while node.left is not None:
        parent = node
        node = node.left

    return node

def search_min_node_from_right_np(root):
    node = root.right
    parent = root
    while node.left is not None:
        parent = node
        node = node.left

    parent.left = None

    return node

def get_new_root(node, parent, root):
    #node_list = search_node_by_key(root, key)

    key = node.value

    # parents exists
    if parent is not None:

        if node.left is None and node.right is None:
            if parent.value <= key:
                parent.right = None
            elif parent.value >= key:
                parent.left = None

        elif node.right is not None or (node.left is not None and (node.value % 2 == 0)):
            min_node_from_right = search_min_node_from_right(node)
            if node.right == min_node_from_right:
                min_node_from_right.right = None
            else:
                node.left = None
                min_node_from_right.right = node.right

            min_node_from_right.left = node.left

            if parent.value <= key:
                parent.right = min_node_from_right
            elif parent.value >= key:
                parent.left = min_node_from_right

        elif node.left is not None:
            max_node_from_left = search_max_node_from_left(node)
            max_node_from_left.right = node.right
            #max_node_from_left.left = node.left

            if parent.value <= key:
                parent.right = max_node_from_left
            elif parent.value >= key:
                parent.left = max_node_from_left

    # no parents
    else:
        if node.right is not None:
            min_node_from_right = search_min_node_from_right_np(node)
            if node.right == min_node_from_right:
                min_node_from_right.right = None
            else:
                min_node_from_right.right = node.right
            min_node_from_right.left = node.left
            root = min_node_from_right
        elif node.left is not None:
            max_node_from_left = search_max_node_from_left(node)
            max_node_from_left.left = node.left
            max_node_from_left.right = node.right
            root = max_node_from_left
        else:
            root = None
    #print(root)
    return root


def remove(root, key):
    return search_node_by_key(root, key)


if __name__ == "__main__":
    def test():

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
        #node7 = Node(None, node6, 5)
        node7 = Node(node3, node6, 5)


        '''
        node2 = Node(None, None, 2)
        node1 = Node(None, node2, 1)
        '''

        '''
        node1 = Node(None, None, 15)
        node2 = Node(node1, None, 20)
        node3 = Node(None, node2, 10)
        '''

        '''
        node1 = Node(None, None, 1)
        node2 = Node(None, None, 3)
        node3 = Node(None, None, 5)
        node4 = Node(None, None, 7)
        node5 = Node(node1, node2, 2)
        node6 = Node(node3, node4, 6)
        node7 = Node(node5, node6, 4)
        '''
        '''
        node1 = Node(None, None, 4)
        node2 = Node(None, node1, 3)
        node3 = Node(None, node2, 2)
        node4 = Node(None, node3, 1)
        '''
        new_node = remove(node7, 10)
        print(new_node)

    test()
