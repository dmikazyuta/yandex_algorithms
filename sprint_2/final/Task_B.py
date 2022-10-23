"""
ID: 67529675

-- ПРИНЦИП РАБОТЫ --
При итерации по входной строке сохраняем численные элементы в стеке.
При получении из строки арифметической операции обращаемся к стеку с использованием pop() два раза,
вычисляем результат и делаем push (append) в стек

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Организация данных в стеке позволяет соблюдать очередность расчета, которую требует польская нотация

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все операции стоят O(1)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В худшем случае мы храним O(n), где n - количество численных элементов в строке до операторов
2 1 2 / *

"""
import operator as op

operations = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.floordiv
}


def calculate(type_oper, number_list):
    b = number_list.pop()
    a = number_list.pop()
    value = operations[type_oper](a, b)
    number_list.append(value)


def work_with_prc():
    input_list = input().split(' ')
    number_list = []

    for i in input_list:
        if i.lstrip("-").isdigit():
            number_list.append(int(i))
        else:
            calculate(i, number_list)
    result = number_list.pop()
    print(result)


if __name__ == "__main__":
    work_with_prc()
