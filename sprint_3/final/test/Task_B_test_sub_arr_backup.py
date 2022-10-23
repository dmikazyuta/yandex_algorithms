def sort_sub_arr(arr, start, end):
    i = start
    left = start
    right = end

    pivot = arr[(end) // 2]
    print(pivot)
    # print(pivot)

    while left <= right:
        if left > i and arr[left] > pivot:
            arr[left], arr[i] = arr[i], arr[left]
            i = i + 1
            left = left + 1
        elif arr[left] < pivot:
            arr[right], arr[i] = arr[i], arr[right]
            right = right - 1
        else:
            left = left + 1

    return left


if __name__ == '__main__':
    persons = [4, 8, 9, 20, 1, 5, 11, 23, 0]
    # persons = [5, 4, 3, 2, 1]
    # arr =

    n = len(persons) - 1
    sort_sub_arr(persons, 0, n)
    print(persons)
