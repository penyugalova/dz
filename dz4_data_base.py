# encoding: utf-8
__author__ = 'Liubov Penyugalova'

import sys
import pickle
import os

#os.getcwd()

#----------объявляем переменные
database     = {}
user_input   = []
same_keys    = []
action       = ''

#---------открываем файл, в котором храняться предыдущие данные, внесенные пользователем
try:
    with open('database.pickle', 'rb') as f:
        file_db = pickle.load(f, encoding="utf-8")
    f.close()
    file_db
except FileNotFoundError:
    file_db = {}


action = input('Нажмите 1 чтобы внести данные. 2 чтобы увидеть весь список. 3 чтобы найти определенный атомобилью 4 чтобы выйти: ')


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






print('Старая БД, которая была в файлике')
print(file_db)

#----------заносим в словарик информацию

if not file_db:
    print(not file_db)
    file_db.update({
        user_input[0][0]:user_input[0][1]
        })

for i in user_input:
    if i[0] in file_db.keys():
        lst = set(file_db.get(i[0]))
        lst.add(i[1])
        file_db.update(
            {
                i[0]:lst
            }
        )
    else:
        file_db.update(
            {
                i[0]:i[1]
            }
        )

#----------дампим словарик с мафынами
f = open('database.pickle', 'wb')
pickle.dump(file_db, f)
f.close()


if action == '2':
    lst = sorted(file_db)
    print('Обычная сортировка')
    for i in lst:
        print(i, ':', file_db.get(i))


#----------------пузырьковая сортировка
if action == '2':
    lst = list(file_db.keys())
    for n1, i in enumerate(lst):
        for n2, ii in enumerate(lst):
            if i<ii:
                lst[n1], lst[n2] = lst[n2], lst[n1]
    print('Пузырьковая сортировка')
    for i in lst:
        print(i, ':', file_db.get(i))


if action == '3':
    user_input =



sys.exit(0)
'''
1. Сделайте простую базу данных:

Пользователь вводит команду: ввести, вывести
- Вывести - выводятся все автомобили - по алфавиту. Сортировку сделать сначала стандартным методом. Затем написать свою версию сортировки циклами.

- вывести пл
2. Реализовать поиск/фильтрацию в базе данных - то есть вывод по условию.

- По мощности - конкретное число, больше, меньше, в промежутке.
- По вхождению слова в название.
- По полному соответствию слова.
'''