"""
Гардероб

В первой строке задано количество предметов в гардеробе:
n –— оно не превосходит 1000000.

Во второй строке даётся массив, в котором указан цвет
для каждого предмета.

Сначала должны идти вещи розового цвета,
потом —– жёлтого,
и в конце —– малинового

Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.

"""


def count(arr):
    dict_a = {}
    for key in arr:
        dict_a[key] = dict_a.get(key, 0) + 1
    return dict_a


def wardrobe(arr):
    count_dict = count(arr)
    result_list = [0] * count_dict.get('0', 0) + \
                  [1] * count_dict.get('1', 0) + \
                  [2] * count_dict.get('2', 0)

    print(*result_list)


if __name__ == "__main__":
    n = int(input())
    arr = input().split(' ')
    wardrobe(arr)
