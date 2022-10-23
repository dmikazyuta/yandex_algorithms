def sort_sub_arr(arr, start, end):
    i = start
    left = start
    right = end

    pivot = arr[(end + 1) // 2]
    print(pivot)
    # print(pivot)

    while left <= right:
        if i > left and arr[i] > pivot:
            arr[i], arr[left] = arr[left], arr[i]
            #i = i + 1
            left = left + 1
        elif arr[right] < pivot:
            arr[right], arr[left] = arr[right], arr[right]
            right = right - 1
        else:
            i = i + 1

    return left


if __name__ == '__main__':
    persons = [4, 8, 9, 20, 1, 5, 11, 23, 0]
    # persons = [5, 4, 3, 2, 1]
    # persons = [-10, -9, -8, -7, 0]

    n = len(persons) - 1
    sort_sub_arr(persons, 0, n)

    print(persons)
