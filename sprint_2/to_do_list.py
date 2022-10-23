"""
kazyuta-dv

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

Node('third')
Node('second', n3)
Node('second', n3)

"""


def solution(vertex):
    while vertex:
        print(vertex.value, end="\n")
        vertex = vertex.next_item