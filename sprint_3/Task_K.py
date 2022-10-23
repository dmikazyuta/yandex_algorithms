def get_dict(arr):
    dict_a = {}
    for key in arr:
        dict_a[key] = dict_a.get(key, 0) + 1
    return dict_a


def comparator(a, b, count_dict):
    if a == b:
        return int(a) < int(b)
    else:
        return count_dict[a] < count_dict[b]


def sort_keys_by_values(univer_list, count_dict):
    for i in range(1, len(univer_list)):
        key_item = univer_list[i]
        j = i - 1
        while j >= 0 and comparator(univer_list[j], key_item, count_dict):  # count_dict[univer_list[j]] < count_dict[key_item]
            univer_list[j + 1] = univer_list[j]
            j -= 1
        univer_list[j + 1] = key_item
    return univer_list


def conference_lovers(arr_len, arr, k):
    count_dict = get_dict(arr)
    univer_list = list(count_dict.keys())
    sorted_list = sort_keys_by_values(univer_list, count_dict)

    return sorted_list[:k]


if __name__ == "__main__":
    arr_len = int(input())
    arr = input().split(" ")
    k = int(input())

    result = conference_lovers(arr_len, arr, k)
    print(*result)
