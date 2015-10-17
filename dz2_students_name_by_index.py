#encoding:utf-8

students = ['Alex Blim', 'Stan Krat', 'Rex Rom', 'Don Mahler']

n = len(students)
txt = 'Введите номер студента. Всего их в сиске сейчас {}'
number = input(txt.format(n))

number = number -1

print(students[number])