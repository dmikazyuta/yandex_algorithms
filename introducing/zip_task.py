'''
Даны два массива чисел длины n. Составьте из них один массив длины 2n,
в котором числа из входных массивов чередуются (первый — второй — первый — второй — ...).
При этом относительный порядок следования чисел из одного массива должен быть сохранён.
'''

n = input()
a = input().split(' ')
b = input().split(' ')
result = ''
for i in range(0, int(n)):
    result += ' ' + a[i]
    result += ' ' + b[i]
print(result.strip())