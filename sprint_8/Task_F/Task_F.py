from collections import defaultdict
from functools import cmp_to_key


def compare(next, prev):
    if next[1] > prev[1]:
        return -1
    elif next[1] < prev[1]:
        return 1
    else:
        arr = [next[0],prev[0]]
        arr.sort()
        if arr[0] == next[0]:
            return -1
        else:
            return 1


def find_freq_word(words):
    words_sorted = sorted(words.items(), key=cmp_to_key(compare))
    return words_sorted[0][0]


if __name__ == '__main__':
    n = int(input())
    words = defaultdict(int)
    for i in range(n):
        w = input()
        words[w] += 1

    result = find_freq_word(words)
    print(result)
