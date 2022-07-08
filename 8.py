#Задание 8:
#     Банкомат
#     Напишите код банкомата, который принимает цифру, выдает деньги с номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.
#     Подсказка: напишите функцию, используйте divmod()
nominals = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
summa = int(input('введите нужную сумму '))
ost = 0
ost1 = 0
i = 0
while i <= len(nominals):
    if summa % nominals[i] == 0:
        print(f'{divmod(summa, nominals[i])[0]} купюр по {nominals[i]} сом')
        break
    else:
        ost = summa % nominals[i]
        if divmod(summa, nominals[i])[0] != 0:
            print(f'{divmod(summa, nominals[i])[0]} купюр по {nominals[i]} сом')
            summa -= (nominals[i] * divmod(summa, nominals[i])[0])
    i += 1



