"""
ID: 68339336

Шаги:
1. Создадим для хранения hash таблицы массив list_value по макс допустимой длине 10 ** 5
2. Для расчета индекса воспользуемся формулой для метода умножением, воспользуемся числом Кнута
3. Для удобства работы создадим объекты для каждого уровня:
* Hash Table
* В корзине массива поместим объекты класса Linked List. Имеет методы для вставки, удаления и поиска
* Linked List хранит узлы. Узел Node имеет атрибуты ключ-значение + тех. атрибут для ссылки на сл. узел
4. Отдельно обрабатываем ситуации когда искомый ключ в методе put уже встречался.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(1) в среднем

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В среднем O(n), n - кол-во n - кол-во введенных ключей

"""


def work_with_hash_table():
    class Node:
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next

    class LinkedList:
        def __init__(self):
            self.head = None

        def insert_at_first(self, key, value):
            self.head = Node(key, value, self.head)

        def insert_in_last(self, key, value):
            current = self.head
            if current.key == key:
                self.head = Node(key, value, current.next)
                # return current.value
            else:
                while current.next:
                    current = current.next
                    if current.key == key:
                        current.value = value
                        return
                if current.key == key:
                    current.value = value
                    return
                else:
                    current.next = Node(key, value)

        def find(self, key):
            current = self.head
            while current:
                if current.key == key:
                    return current.value
                current = current.next

        def remove(self, key):
            current = self.head
            previous = None
            if current.key == key:
                cur_value = current.value
                self.head = current.next
                return cur_value
            else:
                while current.next:
                    previous = current
                    current = current.next
                    if current.key == key:
                        previous.next = current.next
                        return current.value

    class HashTable:
        def __init__(self):
            self.size = 10 ** 5
            self.value_list = [None] * self.size
            self.alpha = 20.3951216271

        def hash(self, key: int):
            idx = int(self.size * ((key * self.alpha) % 1))
            return idx

        def put(self, key: int, value: int):
            idx = self.hash(key)
            current = self.value_list[idx]
            if current is not None and current.head is not None:
                self.value_list[idx].insert_in_last(key, value)
            else:
                new_linked_list = LinkedList()
                new_linked_list.insert_at_first(key, value)
                self.value_list[idx] = new_linked_list

        def get(self, key: int):
            idx = self.hash(key)
            value = self.value_list[idx]
            if value is not None and value.head is not None:
                value = value.find(key)
            else:
                value = None
            # print(value)
            return value

        def delete(self, key: int):
            idx = self.hash(key)
            value = self.value_list[idx]
            if value is not None and value.head is not None:
                value = value.remove(key)
            else:
                value = None
            # print(value)
            return value

    htable = HashTable()

    x = ''
    result = []

    n = int(input())
    for i in range(0, n):
        input_list = input().split(" ")

        if input_list[0] == 'put':
            in_key = int(input_list[1])
            in_value = int(input_list[2])
            htable.put(in_key, in_value)

        elif input_list[0] == 'get':
            in_key = int(input_list[1])
            x = str(htable.get(in_key))
            result.append(x)

        elif input_list[0] == 'delete':
            in_key = int(input_list[1])
            x = htable.delete(in_key)
            result.append(x)

    # print(htable.value_list)
    for j in range(0, len(result)):
        print(result[j], end="\n")


if __name__ == "__main__":
    work_with_hash_table()
