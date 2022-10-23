
"""
ID: 68103146

Для реализации quick_sort in-place разделим работу на 3 части:
1. Отсортируем массив относительно pivot элемента как советует условие задачи
2. Отсортируем левую и правую части в рекурсии без возвратов массива, только указатели
Условия выхода оформим для массива с длиной 1 и 2

На вход подается 3 характеристики участника. Составим из них массив.
Для сравнения элементов применим компаратор.

"""


def comparator(greater, lower):
    if greater == lower:
        return False
    if greater[:2] > lower[:2]:
        return True
    elif greater[:2] == lower[:2]:
        return min(greater[2], lower[2]) == greater[2]
    else:
        return False


def sort_sub_arr(arr, start, end):
    i = start
    left = start
    right = end

    pivot = arr[end]

    while i < end and left < right:
        cmprt = comparator(arr[i], pivot)
        if cmprt:
            arr[i], arr[left] = arr[left], arr[i]
            i += 1
            left = left + 1
        elif arr[i] != pivot and not cmprt:
            arr[i], arr[right] = arr[right], arr[i]
            right = right - 1
        else:
            i += 1

    return left


def quick_sort(arr, start, end):
    # Базовый случай
    if start >= end:
        return

    if end == start + 1:
        if arr[start] != arr[end] and not comparator(arr[start], arr[end]):  # arr[start] < arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
            return

    # Сортировка массива
    pivot_idx = sort_sub_arr(arr, start, end)
    # Рекурсивная сортировка левой части
    quick_sort(arr, start, pivot_idx - 1)
    # Рекурсивная сортировка правой части
    quick_sort(arr, pivot_idx + 1, end)


if __name__ == '__main__':

    m = int(input())
    persons = []

    """ 
    Создаем массив с массивами.
    Выстраиваем элементы участника по важности:
    1. Кол-во задач
    2. Кол-во ошибок (умножаем на -1 для того, чтобы большее 
    кол-во ошибок считалось меньшим при сортировке
    3. Имя участника
    """

    for j in range(0, int(m)):
        input_list = input().split(" ")
        persons.append([int(input_list[1]),
                        int(input_list[2]) * -1,
                        input_list[0]])

    n = len(persons) - 1
    quick_sort(persons, 0, n)

    # print(persons)

    for j in range(0, n + 1):
        print(persons[j][2], end='\n')
