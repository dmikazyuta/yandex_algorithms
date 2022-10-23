"""
Соревнование

> 10
> 0 0 1 0 1 1 1 0 0 0

"""


def max_len(data, n):
    hash_table = {}
    prev_balance = -1
    total = 0
    result = 0

    for i in range(0, n):
        d = int(data[i])
        # hash_table[i] = total + d
        if total == 0:
            result = hash_table.get(0, -1) - prev_balance
            print('prev = ' + str(prev_balance))
            prev_balance = hash_table.get(0, -1)
        hash_table[total + d] = i
        total += d

    # result = hash_table[0] - prev_balance
    print('prev = ' + str(prev_balance))
    print(hash_table)
    print('result = ' + str(result))


if __name__ == '__main__':
    n = int(input())
    input_list = input().replace('0', '-1').split()

    max_len(input_list, n)
    #result = max_len(input_list, n)
    #print(result)
