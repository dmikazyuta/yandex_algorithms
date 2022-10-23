import sys

def dfs(var_from, graph, visited, component):
    visited[var_from] = bool(1)
    #print(var_from, end=' ')
    component.append(var_from)
    for var_to in graph[var_from+1]:
        if not bool(visited.get(var_to)):
            dfs(var_to, graph, visited, component)


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
    components = []

    #s = int(input())

    for i in range(0, n):
        if not bool(visited.get(i)):
            current_components = []
            dfs(i, graph, visited, current_components)
            components.append(sorted(current_components))
    components.sort()

    print(len(components))
    for j in components:
        print(*j)

    #dfs(s, graph, visited, components)
