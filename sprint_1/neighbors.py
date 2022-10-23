'''
Дана матрица.
Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево,
вправо, вверх или вниз.
Диагональные элементы соседними не считаются.
'''

n = int(input())
m = int(input())

mx = []
for i in range(0, n):
    mx_new = input().split(' ')
    mx_new = list(map(int, mx_new))
    mx.append(mx_new)

x = int(input())
y = int(input())

result = []
if x - 1 >= 0: result.append(mx[x - 1][y])
if x + 1 <= (n - 1): result.append(mx[x + 1][y])
if y - 1 >= 0: result.append(mx[x][y - 1])
if y + 1 <= (m - 1): result.append(mx[x][y + 1])

result.sort()

result_final = []
j = 0
for j in range(0, len(result)):
    result_final.append(str(result[j]))

print(*result_final)

'''
4
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0
'''