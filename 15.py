# Задание 15:

#     Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#     Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

a = int(input('Введите сумму вклада: '))
years = int(input('Введите сколько лет вы будете вносить свой вклад: '))
for i in range(years):
    b = a * 10 / 100
    a = b + a
print(f'{a} рублей за прошедшие годы')
