# encoding: utf-8
__author__ = 'Liubov Penyugalova'

import sys
import pickle
import os

os.getcwd()

#----------объявляем переменные
database     = {}
file_db      = {}
user_input   = []
action       = ''

action = input('Нажмите 1 чтобы внести данные. 2 чтобы получить информацию. 3 чтобы выйти')

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

file_open()

#----------выявляем и удаляем совпадения ввода пользователя с уже имеющимся в файле

for n, i in enumerate(user_input):
    for ii in file_db:
        if i[0] == ii[0] and i[1] == ii[1]:
            user_input.pop()

#----------заносим в словарик информацию, проверяя, есть ли она уже в файлике
for i in user_input:
    database.update(
        {i[0]:i[1]}
    )

#----------дампим словарик с мафынами
f = open('database.pickle', 'wb')
pickle.dump(database, f)
f.close()


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