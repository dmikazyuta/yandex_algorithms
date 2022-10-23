
def dfs(var_from, graph, visited):
    visited[var_from] = bool(1)
    print(var_from, end=' ')
    for var_to in graph[var_from]:
        if not bool(visited.get(var_to)):
            dfs(var_to, graph, visited)


if __name__ == '__main__':
    graph = {}
    visited = {}

    input_data = input().split(" ")
    n = int(input_data[0])
    m = int(input_data[1])

    for j in range(0, m):
        input_list = map(int, input().split(" "))
