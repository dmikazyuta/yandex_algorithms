"""
ID: 6645151
"""


def near_zero():
    n = int(input())
    lst = input().split(' ')
    lst = list(map(int, lst))
    sublist_result = []

    # collects zeros
    zero_list = [i for i in range(0, n) if lst[i] == 0]

    # iterate by zeros
    for j in range(0, len(zero_list)):

        # first part
        if j == 0 and zero_list[j] > 0:
            for k in range(1, zero_list[j] + 1):
                result_k = zero_list[j] - k + 1
                sublist_result.append(result_k)

        # main part, working with intervals between zeros
        if j != len(zero_list) - 1:

            start = zero_list[j]
            end = zero_list[j + 1]
            sublist_len = end - start - 1
            # starting interval with zero
            sublist_result.append(0)

            for i in range(1, sublist_len + 1):
                # right = i
                # left = left_i
                left_len = end - start
                left_i = abs(left_len - i)
                # compare
                if i > left_i:
                    result_i = left_i
                else:
                    result_i = i
                # append sublist result
                sublist_result.append(result_i)

        # last part
        else:
            for n in range(0, n - zero_list[j]):
                sublist_result.append(n)

    print(*sublist_result)


if __name__ == "__main__":
    near_zero()
