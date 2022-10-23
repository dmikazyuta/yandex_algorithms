"""

"""

buttons = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def curr(input_buttons, buffer, result_list):
    # условие выхода из итерации рекурсии
    if len(buffer) == len(input_str):
        result_list.append(buffer)
        return

    # условие выхода в конце обработки введенных цифр
    for idx in range(0, len(input_buttons)):
        if idx > 0:
            return result_list
        # накопление результата
        input_button = input_buttons[idx]
        symbols = buttons[int(input_button)]
        for symbol in symbols:
            buffer += symbol
            curr(input_buttons[1:], buffer, result_list)
            buffer = buffer[:-1]
        buffer = buffer[:-1]


if __name__ == "__main__":
    input_str = input()
    buffer = ''
    result_list = []

    result = curr(input_str, buffer, result_list)
    print(*result)
