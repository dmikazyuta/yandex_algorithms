from collections import defaultdict


def poly2(letters):
    letters_sorted = sorted(letters.keys(), key=lambda x: x[0])

    poly = str('')
    center = str('')
    for i in letters_sorted:
        if letters[i] == 1 and center == '':
            center = i
        elif letters[i] != 1:
            if letters[i] % 2 == 0:
                m = letters[i] // 2
                poly += i * m
            else:
                if center == '':
                    center = i
                m = (letters[i] - 1) // 2
                poly += i * m

    poly += center + poly[::-1]
    return poly


if __name__ == '__main__':
    input_str = input()
    letters = defaultdict(int)

    for s in input_str:
        letters[s] = letters[s] + 1

    result = poly2(letters)
    print(result)