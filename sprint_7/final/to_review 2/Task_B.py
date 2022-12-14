'''
ID: 71562465

Алгоритм:
Просят проверить можно ли разбить ряд чисел на 2 одинаковые суммы.
Найдем сумму массива и проверим на четность.
Если сумма четная, значит можно искать половину суммы, складывая элементы.
Основная идея - проверить на достижимость при складывании элементов половины суммы.
В массиве с длиной в полусумму будем отмечать флагами элементы, которые взяли из набора очков.
Размещение будем делать справа налево, чтобы избежать пересечений при хранении
(аналогично задаче про золото леприконов)

Пример:
массив очков = 1, 5, 7, 1
полусумма = 14//2 = 7
[0,0,0,0,0,0,0,0] - базовое состояние
[0,1,0,0,0,0,0,0] - положили 1
[0,1,0,0,0,1,1,0] - положили 5, заполняем индексы 5 и 6 (ранее сохраненный 1 + свежий 5)
[0,1,0,0,0,1,1,1] - положили 7, заполняется индекс 7 -> полусумма достижима
и т.д.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(n*s//2), где
n - количество элементов массива очков
s - сумма элементов массива очков

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(s//2 + 1), где
s - сумма элементов массива очков

'''


def same_amounts(points):
    total = sum(points)
    total_half = total // 2

    # проверка на базовый случай, если нечетный -> не можем разбить на 2 суммы
    if total % 2 != 0:
        return 0

    dp = [0] * (total_half + 1)
    for p in points:
        for j in range(total_half, p - 1, -1):
            if dp[j - p] == 1 or j == p:
                dp[j] = 1

    return dp[total_half]


if __name__ == '__main__':
    n = int(input())
    points = list(map(int, input().split(" ")))

    result = bool(same_amounts(points))
    print(result)
