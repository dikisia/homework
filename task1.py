def print_stud():
    print('Колледж Сириус')
    print('Имя:___')
    print('Школа:___')
    print('Группа:___')

print('Автомат для печати бейджиков')
amount = int(input('Количество учеников:'))
for i in range (amount):
    print_stud()
    print('Готово! Заберите бейджики.')