# encoding: utf-8
__author__ = 'Liubov Penyugalova'

import sys
import pickle
import os

#os.getcwd()

#----------объявляем переменные
user_input   = []
same_keys    = []
action       = ''

#---------открываем файл, в котором храняться предыдущие данные, внесенные пользователем
def programma(action):
    global user_input
    global same_keys

    #сздаем ввод информации пользователем

    if action == '1':

        #----------проверяем, отсутствие цифр
        key = input('Введите марку автомобиля:')
        key = key.lower()
        key2 = key.replace(' ', '')


        while key2.isalpha() == False:
            key = input('Ошибка ввода. Введите марку автомобиля:')
            key = key.lower()
            key2 = key.replace(' ', '')
            continue

        #----------проверяем, отсутствие букв
        value = input('Введите его мощность:')
        value_to_check = str(value)
        value_to_check = value_to_check.replace(".","")

        while value_to_check.isnumeric() == False:
            value = input('Ошибка ввода. Введите мощность автомобиля числами (разделитель порядков - точка):')
            value_to_check = str(value)
            value_to_check = value_to_check.replace(".","")
            continue

        #-------------создаем tuple со всеми вводами за "сеанс"

        tup = (key, value)
        user_input.append(tup)
        #action       = ''

        act = input('Нажмите 1 чтобы внести дополнительные данные. 2 чтобы перейти в оснвоное меню: ')

        if act == '2':
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

            #----------дампим словарик с мафынами
            f = open('database.pickle', 'wb')
            pickle.dump(file_db, f)
            f.close()
            act = '5'
            programma(act)
        else:
            pass

    #----------заносим в словарик информацию


    #---------------------------------------------------------СОРТИРОВКА
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

#---------------------------------------------------------------------Выбор автомобиля по параметрам
    if action == '3':
        sec_action = input('Введите 1 для поиска с точным совпадением. Введите 2 для поиска по вххождению слова в название. Введите 3 для поиска по мощности')
        if sec_action == '1':
            user_input = input('Введите марку автомобиля: ')
            user_input = user_input.strip()
            user_input = user_input.lower()
            if user_input in file_db.keys():
                print(user_input, ':', file_db.get(user_input))

        if sec_action == '2':
            user_input = input('Введите элемент марки автомобиля: ')
            user_input = user_input.strip()
            user_input = user_input.lower()

            for i in file_db.keys():
                key_string = str(i)
                if key_string.find(user_input) != -1:
                    print(i, ':', file_db.get(i))

        if sec_action == '3':
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


    if action == '4':
        sys.exit(0)

    if action == '5':
        act = input('Нажмите 1 чтобы внести данные. 2 чтобы увидеть весь список. 3 чтобы найти определенный атомобилью 4 чтобы выйти: ')
        programma(act)

    act = input('Нажмите 1 чтобы внести данные. 2 чтобы увидеть весь список. 3 чтобы найти определенный атомобилью 4 чтобы выйти: ')
    programma(act)

try:
    with open('database.pickle', 'rb') as f:
        file_db = pickle.load(f, encoding="utf-8")
    f.close()
except FileNotFoundError:
    file_db = {}
    action = input('База данных не сформирована. Нажмите 1 чтобы внести данные и создать файл в рабочей директории: ')
    programma(action)


act = input('Нажмите 1 чтобы внести данные. 2 чтобы увидеть весь список. 3 чтобы найти определенный атомобилью 4 чтобы выйти: ')
programma(act)
