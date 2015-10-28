# encoding: utf-8
__author__ = 'Liubov Penyugalova'

import pickle
import os
import sys

# debug.py - вывод на экран + добавила все сопутствующие функции, необходимые для работы программы

def action_func():
    act = input('Нажмите 1 чтобы внести данные. 2 чтобы увидеть весь список. 3 чтобы найти определенный атомобилью 4 чтобы править/удалитью 5 чтобы выйти: ')
    action = act
    return action

def error():
    print('Ошибка ввода!')

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
        import db
        db.pickle_close(user_inp, file)

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


def filter_strict(file_db):
    user_input = input('Введите марку автомобиля: ')
    user_input = user_input.strip()
    user_input = user_input.lower()
    if user_input in file_db.keys():
        print(user_input, ':', file_db.get(user_input))

def filter_non_strict(file_db):
        user_input = input('Введите элемент марки автомобиля: ')
        user_input = user_input.strip()
        user_input = user_input.lower()

        for i in file_db.keys():
            key_string = str(i)
            if key_string.find(user_input) != -1:
                print(i, ':', file_db.get(i))


def filter_power(file_db):
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



def edit(file_db):
    print('Сейчас в базе хранится следующая информация: ')
    print(file_db)
    sec_action = input('Введите 1 для внесения изменений. Введите 2 для удаления элементов.')

    if sec_action == '1':
        key_input   = input('Напечатайте авто, информацию о котором вы хотите изменить: ')
        what_input  = input('Нажмите 1, чтобы исправить название и 2 - мощность: ')
        if  what_input == '1':
           new_input = input('Введите правильное написание: ')
           new_power = file_db.get(key_input)
           file_db.update({new_input:new_power})
           file_db.pop(key_input)
           print('Информация исправлена: ')
           print(file_db)
        else:
           new_power = input('Введите правильную мощность: ')
           trash = file_db.pop(key_input)
           file_db.update(key_input,new_power)
    elif sec_action == '2':
        key_input   = input('Напечатайте авто, информацию о котором вы хотите изменить: ')
        trash = file_db.pop(key_input)
        print('Информация удалена: ')
        print(file_db)
    else:
        pass
