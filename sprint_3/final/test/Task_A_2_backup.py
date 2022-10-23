"""
ID:
"""


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
        # Если k в несортированной части
        mid_var = arr[mid]
        if arr[0] > k:  # arr[mid] < k:
            sub_arr = arr[mid:n]
            result_search = broken_search(sub_arr, k)
            if result_search == -1:
                return -1
            else:
                return mid + result_search
        # Искомый элемент в сортированной части, ура
        else:
            # sub_arr = arr[0:mid - 1]
            # return broken_search(sub_arr, k)
            return binary_search(arr, k, 0, mid)

    # Ищем сортированную часть справа
    else:
        mid_var = arr[mid]
        if arr[mid] < arr[n - 1]:
            # Если k в несортированной части
            mid_var = arr[mid]
            if arr[mid] > k:  # k < arr[mid]:
                sub_arr = arr[0:mid]
                result_search = broken_search(sub_arr, k)
                if result_search == -1:
                    return -1
                else:
                    return result_search
            else:
                # sub_arr = arr[0:mid - 1]
                # return broken_search(sub_arr, k)
                result_search = binary_search(arr, k, mid, n)
                if result_search == -1:
                    return -1
                else:
                    return result_search
        else:
            return -1


if __name__ == "__main__":
    k = int(input())
    arr = list(map(int, input().split(' ')))

    result = broken_search(arr, k)
    print(result)
