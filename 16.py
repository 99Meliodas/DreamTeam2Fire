# Задание 16:
#     Несколько дней подряд метеоролог измеряет температуру воздуха в своём городе.
#     Ваша программа считывает измеренные им значения и выводит среднее значение температуры з
#     а время измерений. Чтобы обозначить конец ввода данных,
#     вводится значение, меньшее -300 (реальная температура не может быть ниже -273.15).
#     При проведении вычислений с действительными числами ответ может незначительно
#     отличаться от математически правильного из-за погрешностей округления;
#     это не повлияет на проверку решения.
########################################################################
gradus = 0
avg_gradus = []
while gradus >= -300:
    gradus = int(input('Введите градус --> '))
    avg_gradus.append(gradus)
    print(sum(avg_gradus) / len(avg_gradus))
