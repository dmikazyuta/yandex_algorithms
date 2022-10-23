'''
def dfs(var_from, graph, visited):
    visited[var_from] = bool(1)
    print(var_from, end=' ')
    for var_to in graph[var_from]:
        if not bool(visited.get(var_to)):
            dfs(var_to, graph, visited)
'''

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


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
    n, m = map(int, input().split(" "))

    graph = read_graph(n, m)
    graph = {'1': set(['2', '3'])
             }
    visited = {}

    s = int(input())

    dfs(graph, s, None)
