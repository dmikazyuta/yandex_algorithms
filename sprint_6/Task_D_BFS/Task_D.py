import queue


def bfs(start, graph, visited):
    q = queue.Queue()
    q.put(start)
    visited[start] = True
    while not q.empty():
        v_from = q.get()
        print(v_from, end=" ")
        for j in graph[v_from]:
            if not bool(visited.get(j)):
                q.put(j)
                visited[j] = True


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