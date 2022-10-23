'''

'''


def same_amounts(n, points):
    total = sum(points)
    total_half = total // 2

    # проверка на базовый случай, нечетный - не можем разбить на 2 суммы
    if total % 2 != 0:
        return 0

    # создаем матрицу
    dp = [([0] + [1] * n) if i != 0
          else [1] * (n + 1)
          for i in range(total_half + 1)]

    #
    for i in range(1, total_half + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1]

            if i >= points[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - points[j - 1]][j - 1])

    return dp[total_half][n]


if __name__ == '__main__':
    n = int(input())
    points = list(map(int, input().split(" ")))

    result = bool(same_amounts(n, points))
    print(result)
