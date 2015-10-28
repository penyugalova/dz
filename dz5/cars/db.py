# encoding: utf-8
__author__ = 'Liubov Penyugalova'

import pickle
import os
import sys

# db.py - чтение и запись данных

#чтение данных
def pickle_open():
    try:
        f = open('database.pickle', 'rb')
        file_db = pickle.load(f, encoding="utf-8")
    except:
        print('Ошибка чтения файла базы данных')
    else:
        file_db = {}
    finally:
        f.close()
        act = input('База данных не сформирована. Нажмите 1 чтобы внести данные и создать файл в рабочей директории. Нажмите 2, чтобы попасть в основное меню: ')
        if act == '1':
            input_data()
        elif act == '2':
            pass
        else:
            pass

    return file_db

#запись данных
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
