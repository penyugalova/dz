#encoding:utf-8

import os

counter = 0
python_files = []
result_file  = ''
w_file       = ''
result       = ''

files = os.listdir('.')

for file in files:
    if file == '.idea' or file == 'first task' or file == 'Coursera.py':
        continue
    connect = open(file, 'r')
    text    = connect.read()
    if text.count('python')>0:
        result = result + '\n' + str(file.encode('utf-8')) + '\n' + str(text.count('python'))

print(result)

result_file = open('result.txt', 'w')
result_file.write(result)
result_file.close()