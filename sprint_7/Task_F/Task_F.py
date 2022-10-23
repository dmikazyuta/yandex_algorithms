

if __name__ == '__main__':
    n, k = map(int, input().split(" "))

    dp = [0] * n
    dp[0] = 1

    for i in range(1,n):
        new_step = max(0, i - k)
        for j in range(new_step, i):
            dp[i] = (dp[i] + dp[j]) % 1000000007
    print(dp.pop())