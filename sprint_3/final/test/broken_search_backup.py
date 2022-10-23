"""
ID:

Алгоритм:
Сломанный массив предполагает наличие 2-х отсортированных частей, внутри которых может быть искомое число k.
Найдем отсортированный подмассив, который содержит k.
После этого применяем к нему классический бинарный поиск.

Учтем крайний случай - массив уже полностью отсортирован (можно сразу вызвать бинарный поиск)

Сложность O(log n), т.к. и на обоих этапах применяется алгоритм бинарного поиска

"""

# Функция классического бинарного поиска для отсортированных интервалов
def binary_search(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


def broken_search(arr, k) -> int:
    n = len(arr)
    mid = n // 2

    # Условие выхода
    if n > 0 and arr[mid] == k:
        return mid

    # Полностью исправный массив
    if arr[0] < arr[n-1]:
        return binary_search(arr, k, 0, n)

    # Ищем сортированную часть слева
    if arr[0] < arr[mid]:
        # Проверяем наличие k
        if arr[0] > k or arr[mid] < k:
            # k в этой части нет, возобновляем поиск в остальном куске массива
            sub_arr = arr[mid:n]
            result_search = broken_search(sub_arr, k)
            if result_search == -1:
                return -1
            else:
                return mid + result_search
        else:
            # k нашелся в этой части, ура
            return binary_search(arr, k, 0, mid)

    # Ищем сортированную часть справа
    else:
        if arr[mid] < arr[n - 1]:
            # Проверяем наличие k
            if arr[mid] > k or k > arr[n - 1]:
                # k в этой части нет, возобновляем поиск в остальном куске массива
                sub_arr = arr[0:mid]
                result_search = broken_search(sub_arr, k)
                if result_search == -1:
                    return -1
                else:
                    return result_search
            else:
                # k нашелся в этой части, ура
                result_search = binary_search(arr, k, mid, n)
                if result_search == -1:
                    return -1
                else:
                    return result_search
        else:
            # k не нашелся
            return -1