def zachet(point:int):
    return point > 50

amount = int(input('Кол-во студентов: '))
for i in range(amount):
    point1 = int(input('Баллы за тест: '))
    total = zachet(point1)
    if total:
        print('Зачет')
    else:
        print('Можете забрать свои документы')