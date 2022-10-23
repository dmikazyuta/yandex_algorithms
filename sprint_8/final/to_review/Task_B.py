'''
ID: 72142758
Алгоритм:
Есть базовое целое слово, есть кандидаты в его составные части.
Потребуется посимвольно разбирать целое слово, проверяя на совпадение с составными словами.

Шаги:
1. Составные слова положим в бор (trie). Потребуется только метод добавления элемента insert
2. Для работы с целым словом дополнительно создадим dp массив, размер = размер слова + 1
Двигаемся по целому слову, проверяем в боре.
Символ может быть терминальным или быть первым в составе составного слова.
Отмечаем его и другие символы слова из бора в dp, делаем это во вложенном цикле.
Головной цикл для экономии итераций идет только по dp[i] = 1, т.е. игнорирует элементы в середине слов или отсутствующие
Наличие внутреннего цикла позволяет захватить все сочетания составных слов.


Если dp[-1] = 1 - значит целое слово удалось разобрать на части полностью.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(L) - заполнение trie, L - суммарная длина слов
O(m**2) - обход в циклах всех символов целого слова
Итог, O(L) + O(m**2)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(m + 1) - dp для целого слова, m - кол-во символов целого слова
O(L) - trie, L - суммарная длина слов
Итог, O(L) + O(m + 1)

'''


class TrieNode:

    def __init__(self, value):
        self.value = value
        self.terminal = False
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):

        node = self.root
        for i in range(len(word)):
            w = word[i]
            if not node.children.get(w, False):
                node.children[w] = TrieNode(w)
            node = node.children.get(w, '')

        node.terminal = True


def check_word(whole_word, trie):
    dp = [1] + [0] * len(whole_word)
    for i in range(len(whole_word)):
        if dp[i]:
            # возвращаемся к головному узлу дерева
            node = trie.root
            # старт от i элемента для захватывания всех сочетания составных слов
            for j in range(i, len(whole_word) + 1):

                # отметим узлы, которые являются терминальными
                if node is not None and node.terminal:
                    dp[j] = 1

                # Двигаемся по дереву, условия прерывания:
                # 1. элемент является последним в слове
                # 2. элемент НЕ является потомком предыдущего узла дерева, т.о. прерывается поиск составного слова
                if j < len(whole_word) and node.children.get(whole_word[j], False):
                    node = node.children[whole_word[j]]
                else:
                    break

    return dp[-1]


if __name__ == '__main__':
    whole_word = input()
    n = int(input())

    trie = Trie()
    for i in range(n):
        word = input()
        trie.insert(word)

    #node = trie.search('exam')
    result = check_word(whole_word, trie)
    if bool(result):
        print('YES')
    else:
        print('NO')