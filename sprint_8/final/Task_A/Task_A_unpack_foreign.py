
def unpack(string):
    multiply, symbol, result = [], [], []
    for char in string:
        if char.isnumeric():
            multiply.append(int(char))
            continue
        if char == '[':
            symbol.append([])
            continue
        if char == ']':
            if len(symbol) == 1:
                result.append(''.join(symbol.pop()) * multiply.pop())
                continue
            previous = ''.join(symbol.pop())
            symbol[-1].append(previous * multiply.pop())
            continue
        if len(symbol) == 0:
            result.append(char)
            continue
        symbol[-1].append(char)

    return ''.join(result)


if __name__ == '__main__':
    word = input()
    result = unpack(word)
    print(result)