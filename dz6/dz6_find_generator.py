# encoding: utf-8
__author__ = 'Liubov Penyugalova'


import os

#1. Создайте функцию-генератор find, которая будет заходить в директорию и рекурсивно бежать по всем файлам и папкам, то есть:
root        = r'C:\test'
file_type   = 'txt'
sub_str = 'print'

def find_generator(rootdir, f_type):
        #Смотрит содержимое папки
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
    #Читает содержимое каждого файла с заданным расширением (например, txt) - по очереди.
            try:
                rasshirenie = file[(file.index('.')+1):]
            except:
                rasshirenie = 'none'
            if not rasshirenie:
                rasshirenie = 'none'
            if rasshirenie == f_type:
#                try:
#                    connect = open(os.path.join(subdir, file), 'r')
#                    text    = connect.read()
#                    connect.close()
#                except:
#                    continue

#            else:
#                continue
            yield file

lines = (subdir, dirs, files for subdir, dirs, files in os.walk(rootdir) if file[(file.index('.')+1):] == sub_str)


#2. Создать функцию-генератор grep, которая будет получать на вход генератор и фильтровать его по вхождению строки, то есть:
#На входе генератор и искомая подстрока.

def grep_generator(find_string, f_generator):
    #По циклу - если в текущей строке найдена подстрока, то по yield выводит имя файла, номер строки и строку.

    for i in {x:y for y, x in f_generator(root, file_type)}.items():
        for line in i[1]:
            #if i[1].find(find_string):
            if line.find(find_string):
                #По циклу - если в текущей строке найдена подстрока, то по yield выводит имя файла, номер строки и строку.
                #файл читается не по строкам (все содер), поэтому затрудняюсь вывести строчку, но имя файла - не вопрос.
                print(i[0], line)


#3. Сделайте программу, ищущую с помощью этих 2-ух генераторов строки в файлах с расширением .py, в которых встречается, например,
# определенный тип исключений "TypeError" или, например, инструкция "def".
#Собственно программа будет выглядеть из запуска
grep_generator(sub_str, find_generator)





def find():



def grep(pattern, lines):
    return (line for line in lines if pattern in lines)


grep(sub_str, find_generator)



#                    print(os.path.join(subdir, file))

#Выдает через yield имя файла, номер строки и строку.