'''
ID: 71520814

Алгоритм:
Используем алгоритм определения редакционного расстояния Ливенштейна
По Ливенштейну расстояние F для слов A и B будет находиться:
1. F(i-1)(j-1), если последний символ одинаковый A(i) = B(j)
2. 1 + min(F(i-1)j, Fi(j-1), F(i-1)(j-1)), если последний символ не одинаков A(i) <> B(j)

Опирался на теорию:
Вики https://ru.wikipedia.org/wiki/Расстояние_Левенштейна
Лекуия МФТИ https://youtu.be/rEPggzaPoUw

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(n + m), где
n - длина первого слова
m - длина второго слова

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O (n * m), где
n - длина первого слова
m - длина второго слова

'''


def levenstein(fw, sw):
    n = len(fw)
    m = len(sw)

    # сгенерируем матрицу
    # i * j == 0 - аналог i == 0 or j == 0
    dp = [[(i + j) if i * j == 0 else 0
               for j in range(m + 1)]
              for i in range(n + 1)]

    # обход матрицы
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if fw[i-1] == sw[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],
                                   dp[i][j-1],
                                   dp[i-1][j-1])

    print(dp[n][m])


if __name__ == '__main__':
    first_word = input()
    second_word = input()

    levenstein(first_word, second_word)
