# Задание 1:
# У вас есть идея создать Back-end для игры: "Угадай число."
# Данный код генерирует рандомное число.
###################

import random as rd
random_number = rd.randint(0,10)
print(random_number)
i = 3
while i != 0:
    a = int(input('Отгадайте число: '))
    if a == random_number:
        print("Вы отгадали число!")
        break
    else:
        i -= 1
        print(f'Неверно! У вас осталось {i} попыток!')

