def comparator(a, b):
    return int(b + a) > int(a + b)


def insertion_sort(n, array):
    for i in range(1, n):
        key_item = array[i]
        j = i - 1
        while j >= 0 and comparator(array[j], key_item): #array[j] < key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array



    result = "".join(insertion_sort(n, m))
    print(result)
