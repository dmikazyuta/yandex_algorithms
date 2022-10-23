"""

16
0 0 1 0 0 1 1 1 1 1 0 0 0 0 0 1

>> 14

"""


def max_len(data, n):
    hash_table = {}
    total = 0
    max_len = 0

    for i in range(0, n):
        total += int(data[i])
        if total == 0:
            max_len = i + 1
        elif hash_table.get(total):
            max_len = max(max_len, i - hash_table[total])
        else:
            hash_table[total] = i

    return max_len


if __name__ == '__main__':
    n = int(input())
    try:
        input_str = str(input())
        input_list = input_str.replace('0', '-1').split()
        result = max_len(input_list, n)
        print(result)
    except:
        print('0')


