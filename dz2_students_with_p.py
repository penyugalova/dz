#encoding:utf-8

students = ['Alex Plim', 'Stan Krat', 'Pex Rom', 'Don Mahler']

for name in students:
    name2 = str(name).lower()
    if name2.find('p')!= -1:
        print (name)
    else:
        continue