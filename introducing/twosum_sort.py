'''
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.

алгоритм с сортировкай
'''

n = int(input())
q = input().split(' ')
k = int(input())

q = list(map(int, q))
result = None

q.sort()
left = 0
right = n - 1

while left < right:
    print("a = " + str(q[left]) + "; " + "b = " + str(q[right]))
    current_sum = q[left] + q[right]
    if current_sum == k:
        result = str(q[left]) + ' ' + str(q[right])
        break
    else:
        if current_sum < k:
            left += 1
        else:
            right -= 1

print(result)


