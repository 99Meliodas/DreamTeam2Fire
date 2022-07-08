# Задание 14:
#     Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
#####################################################################
def season(number):
    di ={1:'Январь',
         2:'Февраль',
         3:'Март',
         4:'Апрель',
         5:'Май',
         6:'Июнь',
         7:'Июль',
         8:'Август',
         9:'Сентябрь',
         10:'Октябрь',
         11:'Ноябрь',
         12:'Декабрь'}
    if number == 12 or number == 1 or number == 2:
         print(di.get(number, 'Такого месяца нет!'))
         return 'Winter'
    if number == 3 or number == 4 or number == 5:
         print(di.get(number, 'Такого месяца нет!'))
         return 'Spring'
    if number == 6 or number == 7 or number == 8:
         print(di.get(number, 'Такого месяца нет!'))
         return 'Summer'
    if number == 9 or number == 10 or number == 11:
         print(di.get(number, 'Такого месяца нет!'))
         return 'Winter'
    return di.get(number, 'Такого месяца нет!')
number = int(input('Введите номер месяца --> '))
print(season(number=number))
