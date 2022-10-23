
def get_unpack_word(word):
    start_stack = []
    subword_list = []

    for i in range(0, len(word)):
        w = word[i]
        if word[i].isdigit():
            start_stack.append(i + 1)
        elif word[i] == ']':
            pass
        elif word[i] != '[':
            subword_list.append(word[i])


if __name__ == '__main__':
    word = input()
    result = get_unpack_word(word)
    print(result)