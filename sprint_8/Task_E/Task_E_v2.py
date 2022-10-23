
def modify_word(basic_word, insertions):
    cur = 0
    result = ''
    for insertion in insertions:
        p = int(insertion[1])
        s = insertion[0]
        while cur != p:
            result += basic_word[cur]
            cur += 1

        if cur == p:
            result += s

    for j in range(basic_word):
        result += basic_word[j]

    return result


if __name__ == '__main__':
    basic_word = input()
    n = int(input())

    insertions = []
    for i in range(n):
        insertions.append(list(input().split(" ")))

    result = modify_word(basic_word, insertions)
    print(result)