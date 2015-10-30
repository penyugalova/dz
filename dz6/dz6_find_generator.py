# encoding: utf-8
__author__ = 'Liubov Penyugalova'


import os


#1. Создайте функцию-генератор find, которая будет заходить в директорию и рекурсивно бежать по всем файлам и папкам, то есть:
#Смотрит содержимое папки.
#Читает содержимое каждого файла с заданным расширением (например, txt) - по очереди.

def find(root, file_type):
    for dict in (({subdir:files} ) for subdir, dirs, files in os.walk(root)):
        for key in dict.keys():
            for file in dict.get(key):
                if file[(file.index('.')+1):] == file_type:
                    d = os.path.join(key,file)
                    for line in open(d):
                        yield line, file


#2. Создать функцию-генератор grep, которая будет получать на вход генератор и фильтровать его по вхождению строки, то есть:
#На входе генератор и искомая подстрока.
#По циклу - если в текущей строке найдена подстрока, то по yield выводит имя файла, номер строки и строку.

def grep(find_gen, sub_str):
    line_counter = 0
    for line, file in find_gen:
        line_counter += 1
        if line.find(sub_str) != -1:
            yield file, line, line_counter


#3. Сделайте программу, ищущую с помощью этих 2-ух генераторов строки в файлах с расширением .py,
# в которых встречается, например, определенный тип исключений "TypeError" или, например, инструкция "def".

root        = r'C:\test'
file_type   = '.py'
sub_str = 'def'

for file, line, line_counter in grep(find(root, file_type), sub_str):
    print(file, line, line_counter)

