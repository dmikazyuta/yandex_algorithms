'''
ID:
Алгоритм:

'''


class TrieNode:

    def __init__(self, value):
        self.value = value
        self.terminal = False
        self.level = 0
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
                node.level = i + 1
            else:
                new_node = TrieNode(word[i])
                node.children[word[i]] = new_node
                node = new_node
                node.level = i + 1

        node.terminal = True

    def search(self, char):
        node = self.root

        for c in char:
            if c in node.children:
                node = node.children[c]
            else:
                return None

        return node


def check_word(whole_word, trie):
    dp = [1] + [0] * len(whole_word)

    for i in range(len(whole_word)):
        node = trie.root
        if dp[i]:
            for j in range(i, len(whole_word) + 1):
                wh = whole_word[j:]

                if node is not None and node.terminal:
                    dp[j] = 1

                # последний элемент
                if j == len(whole_word) or not node.children.get(whole_word[j], False):
                    break
                node = node.children[whole_word[j]]

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