
def get_mod_word(word):
    mod_word = ''
    for w in word:
        if ord(w) % 2 == 0:
            mod_word += w
    return mod_word


def compare_words(aw, bw):
    mod_aw = get_mod_word(aw)
    mod_bw = get_mod_word(bw)

    if mod_aw < mod_bw:
        return -1
    elif mod_aw == mod_bw:
        return 0
    else:
        return 1


if __name__ == '__main__':
    a_word = input()
    b_word = input()

    result = compare_words(a_word, b_word)
    print(result)
