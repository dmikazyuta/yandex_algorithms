"""
Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке.
Класс должен поддерживать операции push(x),
где x – целое число, pop() и get_max().

8
get_max
push 7
pop
push -2
push -1
pop
get_max
get_max

"""


def stack_max():
    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            if len(self.items) > 0:
                self.items = self.items[:-1]
            else:
                print('error')

        def get_max(self):
            mx = 'None'
            if len(self.items) > 0:
                mx = str(max(self.items))
            print(mx)

    n = int(input())
    stack = Stack()

    for i in range(0, n):
        input_str = input()
        if input_str == 'get_max':
            stack.get_max()
        if input_str == 'pop':
            stack.pop()
        if input_str[:4] == 'push':
            len_str = len(input_str)
            input_num = int(input_str[5:len_str])
            stack.push(input_num)


if __name__ == "__main__":
    stack_max()
