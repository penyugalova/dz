# encoding: utf-8
__author__ = 'Liubov Penyugalova'

import sys
import pickle
import os
import sys

#1.1 Берем задачу из дз №3. Выделяем следующие процессы в функции: ввод команды - отдельная функция

def action_func():
    act = input('Нажмите 1 чтобы внести данные. 2 чтобы увидеть весь список. 3 чтобы найти определенный атомобилью 4 чтобы выйти: ')
    action = act
    return action

#1.2 Берем задачу из дз №3. Выделяем следующие процессы в функции:  сообщение в случае ошибки ввода команды - отдельная функция

def error():
    print('Ошибка ввода!')

#1.3 Берем задачу из дз №3. Выделяем следующие процессы в функции:  Ввести и Вывести - 2 отдельные функции

#ввести
def input_data(file):
    user_input = []

    key = input('Введите марку автомобиля:')
    key = key.lower()
    key2 = key.replace(' ', '')


    while key2.isalpha() == False:
        error()
        key = input('Введите марку автомобиля:')
        key = key.lower()
        key2 = key.replace(' ', '')
        continue

    value = input('Введите его мощность:')
    value_to_check = str(value)
    value_to_check = value_to_check.replace(".","")

    while value_to_check.isnumeric() == False:
        error()
        value = input('Введите мощность автомобиля числами (разделитель порядков - точка):')
        value_to_check = str(value)
        value_to_check = value_to_check.replace(".","")
        continue

    tup = (key, value)
    user_input.append(tup)

    act = action_func()

    if act == 1:
        input_data()
    else:
        user_inp = user_input
        pickle_close(user_inp, file)



#вывести

def show_data(file_db):
    lst_1 = sorted(file_db)
    print('Обычная сортировка')
    for i in lst_1:
        print(i, ':', file_db.get(i))

    lst_2 = list(file_db.keys())
    for n1, i in enumerate(lst_2):
        for n2, ii in enumerate(lst_2):
            if i<ii:
                lst_2[n1], lst_2[n2] = lst_2[n2], lst_2[n1]
    print('Пузырьковая сортировка')
    for i in lst_2:
        print(i, ':', file_db.get(i))


#1.4 Берем задачу из дз №3. Выделяем следующие процессы в функции:  поиски по условию - 3 отдельные функции соответственно

def filter_strict():
    user_input = input('Введите марку автомобиля: ')
    user_input = user_input.strip()
    user_input = user_input.lower()
    if user_input in file_db.keys():
        print(user_input, ':', file_db.get(user_input))

def filter_non_strict():
        user_input = input('Введите элемент марки автомобиля: ')
        user_input = user_input.strip()
        user_input = user_input.lower()

        for i in file_db.keys():
            key_string = str(i)
            if key_string.find(user_input) != -1:
                print(i, ':', file_db.get(i))


def filter_power():
    user_input = input('Введите мощность автомобиля одной или двумя (если интересует промежуток) цифрами с пробелом: ')
    user_input = user_input.strip()
    user_input = user_input.split()
    if len(user_input) == 1:
        for i in file_db.keys():
            if type(file_db.get(i)) == str:
                val = [file_db.get(i)]
            else:
                val = file_db.get(i)
            if len(val) > 1:
                for ii in val:
                    if user_input[0] == ii:
                        print(i, ':', ii)
            else:
                if user_input[0] == val[0]:
                    print(i, ':', val[0])


    elif len(user_input) == 2:
        n1 = int(user_input[0])
        n2 = int(user_input[1])

        if n1 > n2:
           n1, n2 = n2, n1

        for i in file_db.keys():
            if type(file_db.get(i)) == str:
                val = [file_db.get(i)]
            else:
                val = file_db.get(i)
            if len(val) > 1:
                for ii in val:
                    if int(ii) >= n1 and int(ii) <= n2:
                        print(i, ':', ii)
            else:
                if int(val[0]) >= n1 and int(val[0]) <= n2:
                    print(i, ':', val[0])
    else:
        user_input = input('Неверно указана мощность.')

#1.5 Берем задачу из дз №3. Выделяем следующие процессы в функции:  сохранение в pickle и загрузка из pickle - 2 отдельные функции

#загрузка
def pickle_open():

    try:
        f = open('database.pickle', 'rb')
        file_db = pickle.load(f, encoding="utf-8")
        f.close()
    except:
        file_db = {}
        act = input('База данных не сформирована. Нажмите 1 чтобы внести данные и создать файл в рабочей директории. Нажмите 2, чтобы попасть в основное меню: ')
        if act == '1':
            input_data()
        elif act == '2':
            pass
        else:
            pass
    return file_db

#сохранение
def pickle_close(user_input, file_db):
    if not file_db:
        file_db.update({
        user_input[0][0]:user_input[0][1]
        })

    for i in user_input:
        if i[0] in file_db.keys():
            if type(file_db.get(i[0])) == str:
                val = [file_db.get(i[0])]
            else:
                val = file_db.get(i[0])
            lst = set(val)
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
    f = open('database.pickle', 'wb')
    pickle.dump(file_db, f)
    f.close()

# функция самой программы
def programma(act):
    if act == '1':
        file_db = pickle_open()
        input_data(file_db)
        action = action_func()
        programma(action)
    elif act == '2':
        file_db = pickle_open()
        file = file_db
        show_data(file)
        action = action_func()
        programma(action)
    elif act == '3':

        sec_action = input('Введите 1 для поиска с точным совпадением. Введите 2 для поиска по вххождению слова в название. Введите 3 для поиска по мощности')

        if sec_action == '1':
            filter_strict()
        elif sec_action == '2':
            filter_non_strict()
        elif sec_action == '3':
            filter_power()
        else:
            error()
            action = action_func()
            programma(action)
    elif act == '4':
        sys.exit()
    else:
        error()
        action = action_func()
        programma(action)
    action = action_func()
    programma(action)



file_db = pickle_open()
act = ''
action = action_func()
programma(action)