minimum_spanning_tree = []   # Рёбра, составляющие MST.

added = {}          # Множество вершин, уже добавленных в остов.
not_added = {}      # Множество вершины, ещё не добавленных в остов. 
edges = []          # Массив рёбер, исходящих из остовного дерева.


# Перестраиваем массив в бинарную кучу
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Левый потомок меньше, чем родитель
    if left < n and arr[i] > arr[left]:
        largest = left

    # Правый потомок меньше, чем родитель
    if right < n and arr[largest] > arr[right]:
        largest = right

    # Смена родителя
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)


def heap_sort(arr, n):
    # Обход кучи снизу
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Обход кучи снизу
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)


def add_vertex(graph, v):
    global added
    global not_added
    global edges
    global minimum_spanning_tree

    added += v
    not_added -= v
    edges += graph.edges.filter(start == v, end in not_added) # ?


def find_MST(graph):
    global added
    global not_added
    global edges
    global minimum_spanning_tree

    not_added = graph.verices

    v = graph.verices[0]
    add_vertex(graph, v)

    while len(not_added) > 0 and len(edges) > 0:
        heap_sort(edges, len(edges)) # len(edges) - ?
        # e = extract_minimum(edges)
        e = edges[0]

        if e.end in not_added:
            minimum_spanning_tree += e
            add_vertex(graph, e.end)

    if len(not_added) > 0:
        print("oops")
    else:
        return minimum_spanning_tree

