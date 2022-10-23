

def bubble(n, arr):
    arr_prev = []
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if arr_prev != arr:
            print(*arr)
            arr_prev = arr.copy()


if __name__ == "__main__":
    n = int(input())
    m = input().split(' ')
    arr = [int(numeric_string) for numeric_string in m]
    bubble(n, arr)
