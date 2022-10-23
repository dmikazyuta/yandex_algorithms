
def lets_modify_word(bw, nw, k):
    nw_str = nw[0]
    nw_idx = int(nw[1])
    l = len(nw_str) + k

    if nw_idx == 0:
        return bw[0:nw_idx] + nw_str + bw[nw_idx:], l
    return bw[0:nw_idx + k] + nw_str + bw[nw_idx + k:], l


if __name__ == '__main__':
    basic_word = input()
    n = int(input())

    arr = []
    k = 0
    for i in range(n):
        new_word = list(input().split(" "))
        basic_word, k = lets_modify_word(basic_word, new_word, k)

    print(basic_word)
