'''
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.

алгоритм с search data structure
'''

n = int(input())
q = input().split(' ')
k = int(input())

q = list(map(int, q))
result = None
previos = set()

for i in range(0, n):
    b = k - q[i]
    print('i = ' + str(i))
    print('q[i] = ' + str(q[i]))
    print('b = ' + str(b))
    if b in previos:
        result = str(q[i]) + ' ' + str(b)
    else:
        print('added')
        previos.add(q[i])

print(result)

