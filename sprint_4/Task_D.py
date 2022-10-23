"""

Кружки

"""


def hash_key(dict_a, a):
    return bool(dict_a.get(a, 0))


if __name__ == "__main__":
    hobby_community = {}
    n = int(input())
    for j in range(0, n):
        hobby = input()

        if not hash_key(hobby_community, hobby):
            hobby_community[hobby] = 0
            print(hobby, end='\n')
        hobby_community[hobby] += 1


