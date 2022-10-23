
if __name__ == '__main__':
    n = int(input())
    left = 1
    right = 1
    for i in range(n):
        #print(i)
        left, right = right, left
        right = (left + right) % 1000000007

    print(left)