"""
ID: 66455517
"""

k = int(input())
input_str = input()
input_str += input()
input_str += input()
input_str += input()

input_list = [int(x) for x in input_str if x.isdigit()]

dict_numbers = {}
for num in input_list:
    dict_numbers[num] = dict_numbers.get(num, 0) + 1

points = 0
for i in dict_numbers:
    if dict_numbers[i] <= k * 2:
        points += 1

print(str(points))
