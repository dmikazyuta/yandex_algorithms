from collections import deque


def bfs(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    while len(q) != 0:
        first_vertex = q.popleft()
        print(first_vertex, end=" ")
        for i in graph[first_vertex]:
            if not bool(visited.get(i)):
                q.append(i)
                visited[i] = True


def read_graph(n, m):
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
    visited = {}
    s = int(input())

    bfs(s, graph, visited)