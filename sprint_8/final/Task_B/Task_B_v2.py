class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = {} if next is None else next
        self.terminal = False


def create_tree(words):
    root = Node('')
    for word in words:
        node = root
        for index, char in enumerate(word):
            node.next[char] = node.next.get(char, Node(char))
            node = node.next[char]
        node.terminal = len(word)
    return root


def is_split_words(string, words):
    root = create_tree(words)
    dp = [True] + [False] * len(string)
    for i in range(len(string)):
        node = root
        if dp[i]:
            for j in range(i, len(string) + 1):
                if node.terminal:
                    dp[j] = True

                if j == len(string) or not node.next.get(string[j], False):
                    break
                node = node.next[string[j]]
    return dp[-1]

if __name__ == '__main__':
    string = input()
    words = [input() for _ in range(int(input()))]
    print('YES' if is_split_words(string, words) else 'NO')