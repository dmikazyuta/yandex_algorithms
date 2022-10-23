"""
ID: 71199055

Алгоритм:
Для поиска самой дорогой сети используется алгоритм Прима, реализация с опорой на пример из яндекс уроков.
Дополнительно, обрабатываем ситуацию нескольких компонентов связности, одной единственной вершины.
Обрабатываем ситуации, когда есть несколько ребер между одними и теми же вершинами, берем больший вес.

Для списков вершин на добавление используется defaultdict, т.к. понравился более лаконичный синтаксис заполнения
Для поиска максимального элемента используется max по справочнику, по значениям.
Комтест прошел, оставил это решение.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сложность алгоритма Прима + для определения суммы по собранному списку весов ребер затрачивается дополнительное O(E)

O(∣V∣⋅∣E∣ + E), где
V - кол-во вершин
E - кол-во ребер

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Храним:
граф (справочник graph) = O(∣V∣)
справочник для вершин not_added = O(∣V∣)
справочник edges = O(|E|)
финальный лист с весами по кол-ву ребер = O(|E|)

Итого, O(2(∣V∣ + |E|))

"""

import math
from collections import defaultdict


def read_graph():
    not_added = defaultdict(int)
    graph = defaultdict(list)

    n, m = map(int, input().split(" "))
    for j in range(n):
        not_added[j]
    for i in range(m):
        u, v, w = map(int, input().split(" "))
        graph[u - 1].append([v - 1, w])
        graph[v - 1].append([u - 1, w])

    return graph, n, not_added


def add_vertex(v, edges, not_added):

    # ведем справочник необработанных вершин
    not_added.pop(v)

    for i in graph[v]:
        end = i[0]
        w = i[1]
        # Если вершины соединяют несколько ребер с разными весами, то берем ту, у которой
        # больший вес w
        # отриц math.inf работает как заглушка на случай отсутствия дубля ребра
        if not_added.get(end) is not None:
            edges[end] = max(edges.get(end, -math.inf), w)

    return edges

def prim_mst(not_added):

    edges = {}

    v = not_added[0]
    edges = add_vertex(v, edges, not_added)

    while len(not_added) > 0 and len(edges) > 0:
        # Поиск по значениям справочника
        e = max(edges, key=edges.get)
        if not_added.get(e) is not None:
            minimum_spanning_tree.append(edges.pop(e))
            edges = add_vertex(e, edges, not_added)

    return minimum_spanning_tree


if __name__ == '__main__':

    minimum_spanning_tree = []
    graph, n, not_added = read_graph()

    # Обработаем ситуацию с несколькими компонентами связности и ситуацию с единственной вершиной
    if len(not_added) - 1 < len(graph) or len(not_added) == 1:
        minimum_spanning_tree = prim_mst(not_added)
        print(str(sum(minimum_spanning_tree)))
    else:
        print("Oops! I did it again")