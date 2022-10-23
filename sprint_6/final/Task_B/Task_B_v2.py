"""
ID: 71128529

Алгоритм:
Из описания задачи следует, что мы имеем дело с ориентированным графом.
Наличие 2-х видов ребер, позволяющих пройти от вершины к вершине
можно отловить с помощью поиска цикла. Возьмем для R дорог и выполним инвертирование пути.
Например: было 1->R->2, стало 2->1. Механизм инвертирования реализуем сразу в чтении графа.
Поиск цикла осуществим с помощью цветовой раскраски и DFS.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(V+E),
где V - кол-во вершин
E - кол-во ребер

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(V*E),
где V - кол-во вершин
E - кол-во ребер

"""

import sys
from collections import defaultdict


def read_graph_special():
    graph = defaultdict(list)

    n = int(input())
    k = 0
    for u in range(n - 1):
        road_str = input()
        for j in range(1, len(road_str) + 1):
            road = road_str[j - 1]
            if road == 'R':  # делаем реверс направления ребра
                new_u = j + k
                graph[new_u].append(u)
            else:
                graph[u].append(j + k)
        # смещение для вершин в строке, где вводим список дорог
        k += 1

    return graph, n


def dfs(u, color):
    color[u] = "GRAY"
    for v in graph[u]:
        if color[v] == "GRAY":
            return True
        if color[v] == "WHITE" and dfs(v, color):
            return True
    color[u] = "BLACK"
    return False


def check_cycling(graph, n):
    color = ["WHITE"] * n
    for i in range(n):
        if color[i] == "WHITE":
            if dfs(i, color):
                # Если цикл есть, значит дорога не является оптимальной
                return "NO"
    return "YES"


if __name__ == '__main__':
    sys.setrecursionlimit(9999999)

    graph, n = read_graph_special()
    result = check_cycling(graph, n)
    print(result)
