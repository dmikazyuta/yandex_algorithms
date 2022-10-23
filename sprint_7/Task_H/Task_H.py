

if __name__ == '__main__':
    matrix = []

    n, m = map(int, input().split(" "))
    for i in range(n):
        matrix_lst = list(map(int, input()))
        matrix.append(matrix_lst)

    dp = [[0] * (m + 1)] * (n + 1)

    for i in range(n):
        for j in range(m):
            y = n - i - 1
            x = j

            down = dp[y-1][x]
            left = dp[y][x-1]

            dp[y][x] = max(left, down) + matrix[y][x]

    print(dp[1][m-1])