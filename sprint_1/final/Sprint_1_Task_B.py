"""
ID: 66455517
"""


def tricky_hands():
    input_str = ''
    dict_numbers = {}
    k = int(input())
    for i in range(0, 4):
        input_str = input()
        # add to dict
        for x in input_str:
            if x.isdecimal():
                dict_numbers[int(x)] = dict_numbers.get(int(x), 0) + 1

    points = 0
    for i in dict_numbers:
        if dict_numbers[i] <= k * 2:
            points += 1

    print(points)


if __name__ == "__main__":
    tricky_hands()
