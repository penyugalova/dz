# encoding: utf-8
__author__ = 'Liubov Penyugalova'

import sys
import pickle
import os

#os.getcwd()

#----------объявляем переменные
database     = {}
file_db      = {}
user_input   = []
same_keys    = []
action       = ''

action = input('Нажмите 1 чтобы внести данные. 2 чтобы получить информацию. 3 чтобы выйти')
#if action != '1' or action != '3':
#    action = input('Нажмите 1 чтобы внести данные. 2 чтобы получить информацию. 3 чтобы выйти')

#сздаем ввод информации пользователем

while action == '1':

    #----------проверяем, отсутствие цифр
    key = input('Введите марку автомобиля:')
    key2 = key.replace(' ', '')

    while key2.isalpha() == False:
        key = input('Ошибка ввода. Введите марку автомобиля:')
        key2 = key.replace(' ', '')
        continue

    #----------проверяем, отсутствие букв
    value = input('Введите его мощность:')
    value_to_check = str(value)
    value_to_check = value_to_check.replace(".","")

    while value_to_check.isnumeric() == False:
        value = input('Ошибка ввода. Введите мощность автомобиля числами (разделитель - точка):')
        value_to_check = str(value)
        value_to_check = value_to_check.replace(".","")
        continue

    #-------------создаем tuple со всеми вводами за "сеанс"

    tup = (key, value)
    user_input.append(tup)
    action       = ''

    action = input('Нажмите 1 чтобы внести данные. 2 чтобы получить информацию. 3 чтобы выйти')


#---------открываем файл, в котором храняться предыдущие данные, внесенные пользователем

def file_open():
    with open('database.pickle', 'rb') as f:
        file_db = pickle.load(f, encoding="utf-8")
    f.close()
    return file_db

file_db = file_open()

print('Старая БД, которая была в файлике')
print(file_db)

#----------выявляем и удаляем совпадения ввода пользователя с уже имеющимся в файле

for n, i in enumerate(user_input):                                          #бегаем по списку, сформированную пользователем
    for ii in file_db:
        lst = ii[1]                                                         #бегаем по свписку, который уже есть в файле
        if isinstance(lst, list) == True:                                   #проверяем, является ли значение по ключу списком или нет. Он может быть списком, если у модели авто (key) несколько вариантов мощности (value).
            for iii in lst:                                                 #бегаем по листам мощности, если таковые имеются
                if i[0] == ii[0] and i[1] == iii:                           #если и ключ и значение совпадают, удаляем item из списка вводов пользователя
                        user_input.pop(n)
        else:
            if i[0] == ii[0] and i[1] == ii[1]:
                user_input.pop(n)

#----------заносим в словарик информацию + нужна проверка на случай, если пользователь 2 раза сразу ввел сразу два раза одинаковый авто с разной мощностью

if not file_db:
    print(not file_db)
    for i in user_input:
        file_db.update({
            i[0]:i[1]
            })

file_db_upd = file_db.copy()
ui = user_input
for i in user_input:
    for ii in file_db:
        if i[0] == ii:
            lst = [file_db.get(ii)]
            counter = 0
            if isinstance(lst, list) == True:                                #проверяем, является ли значение по ключу списком или нет. Он может быть списком, если у модели авто (key) несколько вариантов мощности (value).
                for iii in lst:
                    if i[1] == iii:
                        pass
                    else:
                        counter += 1
                if counter == len(lst):
                    lst.append(i[1])
                    print('lst в counter')
                    print(lst)
                    file_db_upd.update({
                        i[0]:lst
                    })
            else:
                lst.append(i[1])
                print('lst в не-каунтера')
                print(lst)
                file_db_upd.update({
                    i[0]:lst
                })
        else:
            file_db_upd.update({
                i[0]:i[1]
            })
print(file_db_upd)

#----------дампим словарик с мафынами
f = open('database.pickle', 'wb')
pickle.dump(file_db_upd, f)
f.close()

print('Новая БД, записавшаяся в файлик')
print(file_db_upd)


if action == '3':
    sys.exit(0)


sys.exit(0)
'''
»> import pickle
»> data = {
... 'a': [1, 2.0, 3, 4+6j],
... 'b': ("character string", b"byte string"),
... 'c': {None, True, False}
... }
»>
»> f = open('c:/temp/data.pickle', 'wb')
... pickle.dump(data, f)
...
»> with open('data.pickle', 'rb') as f:
... data_new = pickle.load(f)

1. Сделайте простую базу данных:

Пользователь вводит команду: ввести, вывести
- Ввести - пользователь вводит марку автомобиля и его мощность. Необходимо проверить, что марка состоит только из букв латинского или русского алфавитов. Мощность только из цифр.

- Вывести - выводятся все автомобили - по алфавиту. Сортировку сделать сначала стандартным методом. Затем написать свою версию сортировки циклами.

- вывести пл
2. Реализовать поиск/фильтрацию в базе данных - то есть вывод по условию.

- По мощности - конкретное число, больше, меньше, в промежутке.
- По вхождению слова в название.
- По полному соответствию слова.
'''