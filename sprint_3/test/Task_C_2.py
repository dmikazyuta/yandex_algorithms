def check_subseq(sub_word, word, m, n):
    j = 0
    i = 0

    while j < m and i < n:
        sub_char = sub_word[j]
        char = word[i]
        if sub_char == char:
            j = j + 1
        i = i + 1

    return j == m


if __name__ == "__main__":
    sub_word = input()
    word = input()
    try:
        print(check_subseq(sub_word, word, len(sub_word), len(word)))
    except Exception as err:
        print(err)
