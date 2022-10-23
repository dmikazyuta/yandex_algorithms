
def prefix(words, n):
    if n == 0:
        return 0

    first_word = words[0]

    for l in range(len(first_word) + 1):
        for i in range(n):
            if l == len(words[i]):
                return l
            if words[i][l] != first_word[l]:
                return l


if __name__ == '__main__':
    n = int(input())
    words = []
    for i in range(n):
        w = input()
        words.append(w)

    result = prefix(words, n)
    print(result)
