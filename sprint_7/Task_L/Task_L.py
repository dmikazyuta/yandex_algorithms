
def get_max_weight(n, M, weights):
    dp = [0] * (M + 1)
    dp[0] = 1

    max_weight = 0
    for w in weights:
        for i in range(M, w - 1, -1):
            if dp[i - w] == 1:
                dp[i] = 1
                max_weight = max(max_weight, i)

    return max_weight


if __name__ == '__main__':
    n, M = map(int, input().split(" "))
    weights = map(int, input().split(" "))

    result = get_max_weight(n, M, weights)
    print(result)