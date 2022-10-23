import sys

def dfs(var_from, graph, visited):
    visited[var_from] = bool(1)
    print(var_from, end=' ')
    for var_to in graph[var_from+1]:
        if not bool(visited.get(var_from)):
            dfs(var_from, graph, visited)


def read_graph(n, m):
    #n, m = map(int, input().split(" "))
    graph = {}

    for j in range(0, n):
        graph[j + 1] = []

    for i in range(m):
        u, v = map(int, input().split(" "))
        graph[u].append(v)
        graph[v].append(u)

    for k in graph:
        graph[k].sort()

    return graph


if __name__ == '__main__':
    sys.setrecursionlimit(1500)

    n, m = map(int, input().split(" "))

    graph = read_graph(n, m)
    visited = {}

    s = int(input())

    dfs(s, graph, visited)
