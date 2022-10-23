
def read_graph(n, m):
    matrix = []

    for i in range(n):
        matrix.append([0] * n)

    for j in range(m):
        u, v = map(int, input().split(" "))
        matrix[u-1][v-1] = 1

    return matrix


if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    graph = read_graph(n, m)

    for k in range(0, len(graph)):
        print(*graph[k], end="\n")
