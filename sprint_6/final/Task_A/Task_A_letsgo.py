"""
ID: 70651594

Алгоритм:
Для поиска самой дорогой сети используется алгоритм Прима, реализация с опорой на пример из яндекс уроков.
Дополнительно, обрабатываем ситуацию нескольких компонентов связности, одной единственной вершины.
Обрабатываем ситуации, когда есть несколько ребер между одними и теми же вершинами, берем больший вес.

Для списков вершин на добавление используется defaultdict, т.к. понравился более лаконичный синтаксис заполнения
Для поиска максимального элемента используется max по справочнику, по значениям. Комтест прошел, оставил это решение.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(∣V∣⋅∣E∣ + E), где
V - кол-во вершин
E - кол-во ребер
Для определения суммы по собранному списку весов ребер затрачивается дополнительное O(E)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Храним:
граф (справочник graph) = O(V)
справочники вершин (added и not_added) = O(V)
справочник edges = O(E)
финальный лист с весами ребер = O(E)

O(2(V + E))

"""

import math
from collections import defaultdict

not_added = defaultdict(int)
added = defaultdict(int)
edges = {}

def read_graph():
    global not_added
    graph = defaultdict(list)
    n, m = map(int, input().split(" "))
    for j in range(n):
        not_added[j]
    for i in range(m):
        u, v, w = map(int, input().split(" "))
        graph[u - 1].append([v - 1, w])
        graph[v - 1].append([u - 1, w])

    return graph, n


def add_vertex(v):
    global added
    global not_added
    global edges

    # ведем справочники обработанных и необработанных вершин
    added[v]
    not_added.pop(v)

    for i in graph[v]:
        end = i[0]
        w = i[1]
        # Если вершины соединяют несколько ребер с разными весами, то берем ту, у которой
        # больший вес w
        # отриц math.inf работает как заглушка на случай отсутствия дубля ребра
        if not_added.get(end) is not None:
            edges[end] = max(edges.get(end, -math.inf), w)


def prim_mst(graph, n):
    global not_added
    v = not_added[0]
    add_vertex(v)

    while len(not_added) > 0 and len(edges) > 0:
        # Поиск по значениям справочника
        e = max(edges, key=edges.get)
        if not_added.get(e) is not None:
            minimum_spanning_tree.append(edges.pop(e))
            add_vertex(e)

    return minimum_spanning_tree


if __name__ == '__main__':

    minimum_spanning_tree = []

    graph, n = read_graph()
    # Обработаем ситуацию с несколькими компонентами связности и ситуацию с единственной вершиной
    if len(not_added) - 1 < len(graph) or len(not_added) == 1:
        minimum_spanning_tree = prim_mst(graph, n)
        print(str(sum(minimum_spanning_tree)))
    else:
        print("Oops! I did it again")

