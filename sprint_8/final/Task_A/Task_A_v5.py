def get_unpacked_word(packed_word):
    stack = []
    unpack_word = ''

    for w in packed_word:
        if w.isdigit():
            stack.append([w, ''])
        elif w == '[':
            pass
        elif w.isalpha() and len(stack) > 0:
            stack[-1][1] += w
        elif len(stack) == 0:
            unpack_word += w
        elif w == ']':
            pack_params = stack.pop()
            unpack_sub = int(pack_params[0]) * pack_params[1]
            if len(stack) > 0:
                stack[-1][1] += unpack_sub
            else:
                unpack_word += unpack_sub

    return unpack_word

def find_prefix(aw, bw):
    prefix = ''

    if len(aw) > len(bw):
        bw, aw = aw, bw

    for i in range(len(aw)):
        if aw[i] == bw[i]:
            prefix += aw[i]

    return prefix

if __name__ == '__main__':
    result = get_unpacked_word(input())
    print(result)