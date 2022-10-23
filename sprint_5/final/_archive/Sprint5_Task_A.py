"""

ID: 69984587

Алгоритм:
Разобьем решение на 3 шага:
1. Приведение к куче -- heapify
Оригинальный массив (лист) элементов превращаем в бинарную кучу типа min heap для обратной сортировки
2. Для сравнения элементов листа используем компаратор -- comparator
Для удобства сравнения перестроим массив (лист) элемента с самого сначала и обработаем ситуацию равенства баллов, штрафов
3. После полученной кучи делаем сортировку, меняем элементы местами + повторно восстанавливаем кучу

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сложность приведения к куче O(log n)
Общая сложность O(n * log n), где n - количество элементов

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Корректировка ответа 2022-09-05:
Рекурсивная функция heapify использует стек вызовов. Для хранения стека потребуется O(log n).
Стек вызовов не используется паралельно, вызывается ординарно, поэтому делаю вывод, что общая пространственная сложность -
O(log n), где n - кол-во элементов

"""


# Реализует greater > lower
def comparator(greater, lower):
    if greater == lower:
        return False
    # Сравнение оценок, штрафов в одном массиве
    if greater[:2] > lower[:2]:
        return True
    # Алфавитный порядок
    elif greater[:2] == lower[:2]:
        return min(greater[2], lower[2]) == greater[2]
    else:
        return False

# Перестраиваем массив в бинарную кучу
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Левый потомок меньше, чем родитель
    if left < n and comparator(arr[i], arr[left]):   # arr[i] > arr[l]
        largest = left

    # Правый потомок меньше, чем родитель
    if right < n and comparator(arr[largest], arr[right]):  # arr[largest] > arr[r]
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


if __name__ == '__main__':
    m = int(input())
    persons = []

    for j in range(0, int(m)):
        input_list = input().split(" ")

        # Подготовка массива для удобства передачи в компаратор
        grade = int(input_list[1])
        fail = int(input_list[2]) * -1  # обратная сортировка
        login = input_list[0]

        persons.append([grade, fail, login])

    n = len(persons)

    # Сортировка
    heap_sort(persons, n)

    # Вывод логинов
    for k in range(0, n):
        print(persons[k][2], end='\n')