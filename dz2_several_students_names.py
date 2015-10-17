#encoding:utf-8

students = ['Alex Blim', 'Stan Krat', 'Rex Rom', 'Don Mahler']

n = len(students)

txt = 'Введите номера студентов в формате число:число. Всего в списке сейчас {} студентов.'

number = []

number = input(txt.format(n))

print(students[int(number[0]):int(number[2])])