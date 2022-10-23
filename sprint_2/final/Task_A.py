"""
ID: 67529249

-- ПРИНЦИП РАБОТЫ --

Для реализации дека использую кольцевой буфер.
Каждая сторона дека (front и back) контролируется своей парой узателей.
push и pop операции меняют указатели.
Никаких сортировок или перестроек массива не используем,
фактический порядок хранения элементов нас не интересует.

Указатели:
head - последний добавленый элемент.
Используется для pop. После вызова pop указатель head итерируется -1 внутри кольцевого буфера.
tail - указатель следующего доступного для добавления слота.
Используется для push. После вызова push указатель tail итерируется +1 внутри кольцевого буфера.

Защиту от взаимной перезаписи элементов front и back осуществляет переменная size.
Как только мы заполнили массив, то операции возвращают error.
Также переменная size помогает обрабатывать ситуацию pop по пустому массиву

В случае полной очистки массива (после серии операций pop, например) мы сбрасываем указатели на начальное значение
функцией set_empty().
Это позволяет избежать коллизии итераций. Например, когда
head_back и head_front пересекаются при всё еще доступных слотах массива.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания следует, что front и back стороны контролиются своими указателями,
есть защита от пересечений.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все операции стоят O(1)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Требуется хранить 7 переменных и массив n элементов.
Получается сл. пространственная сложность: O(n+7) ~ O(n)

"""

def work_with_deque():
    class Deque:
        def __init__(self, m):
            # Создаем массив
            self.items = [None] * m
            self.max_m = m
            # Инициируем указатели
            self.head_front = 0
            self.head_back = self.max_m - 1
            self.tail_front = self.head_back
            self.tail_back = 0
            # Начальный размер массива
            self.size = 0

        def is_empty(self):
            return self.size == 0

        # Функция сброса в начальное состояние
        def set_empty(self):
            self.head_front = 0
            self.head_back = self.max_m - 1
            self.tail_front = self.head_back
            self.tail_back = 0

        def push_front(self, value):
            if self.size != self.max_m:
                self.items[self.tail_front] = value
                self.tail_front = (self.tail_front - 1) % self.max_m
                self.size += 1
                self.head_front = (self.tail_front + 1) % self.max_m
            else:
                raise IndexError('error')

        def push_back(self, value):
            if self.size != self.max_m:
                self.items[self.tail_back] = value
                self.tail_back = (self.tail_back + 1) % self.max_m
                self.size += 1
                self.head_back = (self.tail_back - 1) % self.max_m
            else:
                raise IndexError('error')

        def pop_back(self):
            if self.is_empty():
                raise IndexError('error')
            else:
                # Возвращаем элемент
                x = self.items[self.head_back]
                self.tail_back = self.head_back
                self.items[self.head_back] = None
                self.head_back = (self.head_back - 1) % self.max_m
                self.size -= 1
                if self.is_empty():
                    self.set_empty()
                print(x)

        def pop_front(self):
            if self.is_empty():
                raise IndexError('error')
            else:
                x = self.items[self.head_front]
                self.tail_front = self.head_front
                self.items[self.head_front] = None
                self.head_front = (self.head_front + 1) % self.max_m
                self.size -= 1
                if self.is_empty():
                    self.set_empty()
                print(x)

    n = int(input())
    m = int(input())

    deque = Deque(m)

    for i in range(0, n):
        try:
            input_list = input().split()
            if input_list[0] == 'pop_back':
                deque.pop_back()
            if input_list[0] == 'pop_front':
                deque.pop_front()
            if input_list[0] == 'push_front':
                input_num = int(input_list[1])
                deque.push_front(input_num)
            if input_list[0] == 'push_back':
                input_num = int(input_list[1])
                deque.push_back(input_num)
        except IndexError as err:
            print(err)


if __name__ == "__main__":
    work_with_deque()
