def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Левый потомок меньше, чем родитель
    if left < n and arr[i] > arr[left]:   # arr[i] < arr[l]
        largest = left

    # Правый потомок меньше, чем родитель
    if right < n and arr[largest] > arr[right]:  # arr[largest] < arr[r]
        largest = right

    # Смена родителя
    if largest != i:
        (arr[largest], arr[i]) = (arr[i], arr[largest])
        heapify(arr, n, largest)


def heap_sort(arr, n):

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)


if __name__ == '__main__':
    #m = int(input())
    #persons = []
    persons = list(map(int, input().split(" ")))

    '''
    for j in range(0, int(m)):
        input_list = list(map(int, input().split(" ")))

        grade = int(input_list[1])
        fail = int(input_list[2]) * -1  # обратная сортировка
        login = input_list[0]

        persons.append([grade, fail, login])
    '''

    n = len(persons)

    heap_sort(persons, n)
    for k in range(0, n):
        print(persons[k], end='\n')