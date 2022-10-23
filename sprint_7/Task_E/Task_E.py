import math

def get_money_count(M, n, banknotes):
    dp = [0] * (M + 1)

    for i in range(1, M + 1):
        dp[i] = math.inf
        for b in banknotes:
            if b <= i:
                dp[i] = min(dp[i], dp[i - b] + 1)

    if dp[M] == 0 or dp[M] == math.inf:
        return -1
    else:
        return dp[M]


if __name__ == '__main__':
    M = int(input())
    n = int(input())
    banknotes = list(map(int, input().split(" ")))

    result = get_money_count(M, n, banknotes)
    print(result)