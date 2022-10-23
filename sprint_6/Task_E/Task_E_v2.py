import sys


def dfs(v, visited, graph, component):
    visited[v] = True
    component.append(v + 1)
    for to in graph[v]:
        if not visited[to]:
            dfs(to, visited, graph, component)


def read_graph():
    n, m = map(int, input().split(" "))
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    for i in range(n):
        graph[i].sort()

    return graph, n


if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    graph, n = read_graph()
    visited = [False for i in range(n)]
    components = []

    for i in range(n):
        if not visited[i]:
            current_component = []
            dfs(i, visited, graph, current_component)
            components.append(sorted(current_component))
    components.sort()
    print(len(components))
    for c in components:
        print(*c)
