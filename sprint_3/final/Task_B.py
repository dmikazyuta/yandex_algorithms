arr = [4, 8, 9, 20, 1, 5, 3, 10]

n = len(arr) - 1
left = 0
right = n
i = 0

pivot = arr[n]
print(pivot)

while left <= right:

    arr_left = arr[left]
    arr_right = arr[right]

    if arr[left] > pivot:
        arr[right], arr[left] = arr[left], arr[right]
        #left += 1
    elif arr[right] < pivot:
        arr[left], arr[right] = arr[right], arr[left]
        #right -= 1

    left += 1
    right -= 1
    i += 1

#arr[right], arr[left] = arr[left], arr[right]

print(*arr)
