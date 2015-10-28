# encoding: utf-8
__author__ = 'Liubov Penyugalova'

import pickle
import os
import sys

#добавляем путь к файлам данного модуля
sys.path.append(r"C:\Users\аналитик\PycharmProjects\ITMO\dz5\cars")

import db
import debug

# main.py - сама программа. В main.py предусмотреть возможность его импортирования
def programma(act):
    if act == '1':
        file_db = functions.get('pickle_open')()
        functions.get('input_data')(file_db)
        action = functions.get('action_func')()
        programma(action)
    elif act == '2':
        file_db = functions.get('pickle_open')()
        file = file_db
        functions.get('show_data')(file)
        action = functions.get('action_func')()
        programma(action)
    elif act == '3':
        file_db = functions.get('pickle_open')()
        file = file_db
        sec_action = input('Введите 1 для поиска с точным совпадением. Введите 2 для поиска по вххождению слова в название. Введите 3 для поиска по мощности')

        if sec_action == '1':
            functions.get('filter_strict')(file)
        elif sec_action == '2':
            functions.get('filter_non_strict')(file)
        elif sec_action == '3':
            functions.get('filter_power')(file)
        else:
            error()
            action = functions.get('action_func')()
            programma(action)
    elif act == '4':
        file = functions.get('pickle_open')()
        functions.get('edit')(file)
    elif act == '5':
        sys.exit()
    else:
        error()
        action = functions.get('action_func')()
        programma(action)

    action = functions.get('action_func')()
    programma(action)



file_db = db.pickle_open()

functions = {}

functions = {'action_func'      : debug.action_func,
             'error'            : debug.error,
             'input_data'       : debug.input_data,
             'pickle_open'      : db.pickle_open,
             'show_data'        : debug.show_data,
             'filter_strict'    : debug.filter_strict,
             'filter_non_strict': debug.filter_non_strict,
             'filter_power'     : debug.filter_power,
             'edit'             : debug.edit
             }

file_db = functions.get('pickle_open')()
act = ''
action = functions.get('action_func')()

#1. ищем хотя бы 2 места в своей программе, где удобно воспользоваться try - except (задаем полную конструкцию try-except-else-finaly). 2 место
try:
    programma(action)
except:
    print('Произошла ошибка: ' + sys.exc_info()[0])
else:
    print('Попробуйте выбрать другой функционал программы.')
finally:
    action = functions.get('action_func')()
    programma(action)