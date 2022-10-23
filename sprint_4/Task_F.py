"""
Анаграммная группировка

6
tan eat tea ate nat bat
>>
0 4
1 2 3
5

"""


if __name__ == '__main__':
    n = int(input())
    input_list = input().split()

    word_dict = {}

    for i in range(0, n):
        word = input_list[i]
        sorted_word = ''.join(sorted(word))

        word_lst = list(word_dict.get(sorted_word, []))
        word_lst.append(i)
        word_dict[sorted_word] = word_lst

    for j in word_dict:
        print(*word_dict[j], end='\n')
