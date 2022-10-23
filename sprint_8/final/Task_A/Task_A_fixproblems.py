
'''
ID: 71832297

Алгоритм:
Шаги:
1. Распакуем слово -- get_unpacked_word
Итеративно движемся по слову от символа к символу.
Буквы до конструкции n[A] сразу добавляем в переменную ответа unpack_word
Встречаем конструкцию n[A] - сохраняем [n,''] в стек (массив).
Идея в том, чтобы с каждым числом хранился еще и буквенный массив A,
который мы допишем продолжая двигаться по слову до символа ]
Будет так [n,'A'].
Встретили ] - умножим n * A, получим подстроку и вставим ее в предыдущий элемент.
Стек нужен, чтобы выкинуть отработанный элемент и обращаясь через индекс [-1]
дополнить через конкатенацию символьную часть A предыдущего элемента, если есть вложенность.
В конце выведем A, который содержит все распакованные символьные части слова.

2. Найдем префикс -- find_prefix
Найдем префикс сравнивая поэлементно меньшее слово-кандидат с большим словом.
В случае расхождения символов возвращаем результат.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(m1 + n * m2), где
n - кол-во слов
m1 - кол-во символов в запакованном слове
m2 - кол-во символов в распакованном слове

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(2 * n), где
n - большее распакованное слово

'''


def get_unpacked_word(packed_word):
    stack = []
    unpack_word = []

    for w in packed_word:
        if w.isdigit():
            # массив [n, '']
            stack.append([w, ''])
        elif w == '[':
            pass
        # если буква
        elif w.isalpha() and len(stack) > 0:
            # дописываем подстроку A для множителя n -> [n, A]
            stack[-1][1] += w
        # если вне пака [] просто добавим к ответу
        elif len(stack) == 0:
            unpack_word.append(w)
        elif w == ']':
            pack_params = stack.pop()
            unpack_sub = int(pack_params[0]) * pack_params[1]
            # Проверка на финал вложенности n1[A1 n2[A2] ]
            if len(stack) > 0:
                stack[-1][1] += unpack_sub
            else:
                unpack_word.append(unpack_sub)

    return ''.join(unpack_word)


def find_prefix(aw, bw):
    prefix = ''

    if len(aw) > len(bw):
        bw, aw = aw, bw

    for i in range(len(aw)):
        if aw[i] == bw[i]:
            prefix += aw[i]
        else:
            return prefix

    return prefix


if __name__ == '__main__':
    n = int(input()) - 1
    # заранее посчитаем первое слово для поиска префикса
    prefix = get_unpacked_word(input())
    for i in range(n):
        word = get_unpacked_word(input())
        prefix = find_prefix(prefix, word)

    print(prefix)