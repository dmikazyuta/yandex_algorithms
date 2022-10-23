
def read_graph(n, m):
    #n, m = map(int, input().split(" "))
    graph = {}

    for j in range(0, n):
        graph[j + 1] = []

    for i in range(m):
        u, v = map(int, input().split(" "))
        graph[u].append(v)
        #graph[v].append(u)

    for k in graph:
        graph[k].sort()

    return graph


if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    graph = read_graph(n, m)

    for j in graph:
        count = str(len(graph[j]))
        print(count, end=" ")
        print(*graph[j])
