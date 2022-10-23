'''
Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
Измерения велись n секунд.
В секунду i поступает qi запросов.
Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.
'''

n = int(input())
q = input().split(' ')
k = int(input())

cur_sum = 0
result = []

# init cur sum
q = list(map(int, q))
for i in range(0, k):
    cur_sum += q[i]
result.append(cur_sum/k)

# moving avg
for j in range(0, len(q)-k):
    cur_sum -= q[j]
    cur_sum += q[j + k]
    result.append(cur_sum/k)
result_str = map(str, result)
print(' '.join(result_str))