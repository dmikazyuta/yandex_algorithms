def partition(array, low, high):
    pivot = array[high]
    print('pivot = ' + str(pivot))
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


if __name__ == "__main__":
    arr = [4, 8, 9, 20, 1, 5, 3, 10]
    pivot_new = partition(arr, 0, len(arr) - 1)
    print(*arr)
