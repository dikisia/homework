def point(scores):
    """Запрашивает у пользователя баллы по каждому предмету и возвращает их сумму."""
    itog_ocv = 0
    for i in range(scores):
        score = int(input(f'баллы за предмет {i+1}: '))
        itog_ocv += score
    print(f'Итоговое кол-во баллов: {itog_ocv}')
    return itog_ocv


def information(score):
    if score > 80:
        return 'Наградить дипломом.'
    elif score > 50:
        return 'Наградить похвальной грамотой.'
    else:
        return 'Выдать грамоту об участии.'

while True:
    name = input('Введите имя студента (завершить - стоп): ')
    if name == 'стоп':
        break
    if name == 'каплан':
        print('отчислен')
        break
    chislo_predmetov = int(input("Введите число предметов: "))
    score = point(chislo_predmetov)
    information = information(score)
    print(information)