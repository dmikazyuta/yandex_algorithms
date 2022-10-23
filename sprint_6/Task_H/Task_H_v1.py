import sys

T = 0


def dfs(v, used, graph, tin, tout):
    global T
    used[v] = 1
    tin[v] = T
    T += 1
    for to in graph[v]:
        if used[to] == 0:
            dfs(to, used, graph, tin, tout)
    used[v] = 2
    tout[v] = T
    T += 1


def read_graph():
    n, m = map(int, input().split(" "))
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split(" "))
        graph[u - 1].append(v - 1)
    for i in range(n):
        graph[i].sort()
    return graph, n


if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    # graph
    graph, n = read_graph()
    #
    used = [0 for i in range(n)]
    tin = [0 for i in range(n)]
    tout = [0 for i in range(n)]

    for i in range(n):
        if used[i] == 0:
            dfs(i, used, graph, tin, tout)
    for i in range(n):
        print(tin[i], tout[i])