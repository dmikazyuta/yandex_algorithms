"""
def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
"""


def calc_intervals(n):
    interval_starts = []
    interval_ends = []

    for i in range(0, n):
        interval = input().split()
        interval_starts.append(int(interval[0]))
        interval_ends.append(int(interval[1]))

    #insertion_sort(interval_starts)
    #insertion_sort(interval_ends)

    interval_starts = sorted(interval_starts, reverse=True)
    interval_ends = sorted(interval_ends, reverse=True)

    result_list = [interval_starts[0], interval_ends[0]]

    for i in range(1, n):
        if interval_starts[i] > result_list[1]:

            print(*result_list)

            result_list[0] = interval_starts[i]
            result_list[1] = interval_ends[i]

        else:
            result_list[1] = interval_ends[i]

    print(*result_list)


if __name__ == "__main__":
    n = int(input())
    calc_intervals(n)
