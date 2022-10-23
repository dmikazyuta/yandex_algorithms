"""

"""


def comparator(input_greater, input_lower):

    input_greater = input_greater.split(" ")
    input_lower = input_lower.split(" ")

    greater = [int(input_greater[1]),
               int(input_greater[2]) * -1,
               input_greater[0]]

    lower = [int(input_lower[1]),
               int(input_lower[2]) * -1,
               input_lower[0]]

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

    pivot = arr[end + 1 // 2]  # end
    # print(pivot)

    while i < end and left < right:
        if comparator(arr[i], pivot):  # comparator(arr[i], pivot):  # arr[i] > pivot
            arr[i], arr[left] = arr[left], arr[i]
            i = i + 1
            left = left + 1
        elif arr[i] != pivot and not comparator(arr[i], pivot):  # not comparator(arr[i], pivot):  # arr[i] < pivot
            arr[i], arr[right] = arr[right], arr[i]
            right = right - 1
        else:
            i = i + 1

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
    # Рекурсивная сортировка левой (большей) части
    quick_sort(arr, start, pivot_idx - 1)
    # Рекурсивная сортировка правой (меньшей) части
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
        persons.append(input())
        """
        persons.append([int(input_list[1]),
                        int(input_list[2]) * -1,
                        input_list[0]])
        """

    n = len(persons) - 1
    quick_sort(persons, 0, n)

    # print(persons)

    for j in range(0, n + 1):
        print(persons[j].split(' ')[0], end='\n')
