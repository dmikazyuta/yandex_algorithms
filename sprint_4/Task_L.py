"""
L. МногоГоша
"""

def get_hash(str, base, mod):
    hash = 0
    for i in range(0, len(str)):
        hash = (hash * base % mod + str[i]) % mod
    return hash


def get_power(n, base, mod):
    power = 1
    i = 0
    while i < n:
        power = (power * base) % mod
    return power


def get_position(subs_list, str):
    counter = {}
    hash_to_pos = {}
    n = int(subs_list[0])
    k = int(subs_list[1])

    base = 123
    mod = 100003

    hash = get_hash(str[:n], base, mod)
    power = get_power(n, base, mod)

    counter[hash] += 1

    hash_to_pos[hash] = 0
    result = []

    i = 1
    while i + n < len(str):
        hash = (hash + mod - str[i - 1:] * power % mod) % mod
        hash = (hash * base % mod + str[i + n - 1:]) % mod
        counter[hash] += 1

        if counter[hash] == 1:
            hash_to_pos[hash] = i

        if counter[hash] == k:
            result.append(hash_to_pos[hash])

        i += 1

    return result


if __name__ == '__main__':
    subs_list = input().split()
    str = input()
    result = get_position(subs_list, str)
    print(result)