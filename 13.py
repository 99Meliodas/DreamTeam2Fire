# Задание 13:
#     Напишите программу, где исходный список содержит положительные и отрицательные числа. 
#     Требуется положительные поместить в один список, а отрицательные - в другой.

numbers = [-1, 6, -7, -34, 76, -87, -99, 12, 73, 34, -21]
possitive = []
negative = []

for i in numbers:
    if i < 0:
        negative.append(i)
    elif i > 0:
        possitive.append(i)
print(possitive)
print(negative)
    