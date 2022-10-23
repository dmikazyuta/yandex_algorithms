import sys
sys.setrecursionlimit(99999)


def check_subseq(sub_word, word, m, n):
    if m == 0:
        return True
    if n == 0:
        return False

    sub_char = sub_word[m-1]
    char = word[n-1]

    if sub_char == char:
        return check_subseq(sub_word, word, m-1, n-1)
    return check_subseq(sub_word, word, m, n-1)


if __name__ == "__main__":
    sub_word = input()
    word = input()
    try:
        print(check_subseq(sub_word, word, len(sub_word), len(word)))
    except Exception as err:
        print(err)
