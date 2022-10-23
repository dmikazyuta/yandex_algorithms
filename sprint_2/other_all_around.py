"""
Вася решил запутать маму —– делать дела в обратном порядке.
Список его дел теперь хранится в двусвязном списке.
Напишите функцию, которая вернёт список в обратном порядке.


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


node3 = DoubleConnectedNode("node3")
node2 = DoubleConnectedNode("node2")
node1 = DoubleConnectedNode("node1")
node0 = DoubleConnectedNode("node0")


node0.next = node1
node1.prev = node0
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
"""


def solution(node):
    temp = None
    new_head = None
    while bool(node):
        temp = node.prev
        node.prev = node.next
        node.next = temp
        node = node.prev

    if temp is not None:
        new_head = temp.prev

    return new_head
