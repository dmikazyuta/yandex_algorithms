"""
@kazyuta-dv

solution(node0)
node0
node1
node2
node3

#

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def show_lists(node):
    while node:
        print(node.value, end="->")
        node = node.next_item
"""


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node, index):
    head = node
    if index == 0:
        head = node.next_item
        node.next_item = None
    else:
        previous_node = get_node_by_index(node, index - 1)
        next_node = get_node_by_index(node, index + 1)
        previous_node.next_item = next_node
    return head
