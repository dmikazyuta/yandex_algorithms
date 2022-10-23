'''
10
3
8 1
2 10
4 5
'''


def get_max_pack(pack, M):
    pack_sorted = sorted(pack.values(), key=lambda item: int(item[0]), reverse=True)
    result = 0

    for j in pack_sorted:
        price = j[0]
        mass = j[1]

        if M == 0:
            break

        max_weight = min(M, mass)
        result += max_weight * price
        M -= max_weight

    return result


if __name__ == '__main__':
    pack = {}
    M = int(input())

    n = int(input())
    for i in range(n):
        price, mass = map(int, input().split(" "))
        pack[i] = [price, mass]

    result = get_max_pack(pack, M)
    print(result)