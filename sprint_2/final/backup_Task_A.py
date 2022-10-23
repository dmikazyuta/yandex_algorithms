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
                print('error')

        def push_back(self, value):
            if self.size != self.max_m:
                self.items[self.tail_back] = value
                self.tail_back = (self.tail_back + 1) % self.max_m
                self.size += 1
                self.head_back = (self.tail_back - 1) % self.max_m
            else:
                print('error')

        def pop_back(self):
            if self.is_empty():
                print('error')
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
                print('error')
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
        input_str = input()
        input_str_push = input_str[:10]
        len_str = len(input_str)
        if input_str == 'pop_back':
            deque.pop_back()
        if input_str == 'pop_front':
            deque.pop_front()
        if input_str_push == 'push_front':
            input_num = int(input_str[11:len_str])
            deque.push_front(input_num)
        if input_str_push == 'push_back ':
            input_num = int(input_str[10:len_str])
            deque.push_back(input_num)


if __name__ == "__main__":
    work_with_deque()