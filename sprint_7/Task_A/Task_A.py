import itertools

def find_max_profit(n, prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    print(str(profit))


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split(" ")))
    prices_new = [k for k, g in itertools.groupby(prices)]
    find_max_profit(n, prices_new)
