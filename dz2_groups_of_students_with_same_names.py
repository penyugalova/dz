#encoding:utf-8

students = ['Alex Plim', 'Stan Krat', 'Alex Karter', 'Pex Rom', 'Don Mahler', 'Don MacLech', 'Don Stivensson', 'Stan Deroy']

names = []
groups = []


for name in students: #getting all the names
    name = str(name)
    names.append(name.split(" ")[0])

for name in set(names): #creating groups with the same names
    group = []
    for name2 in students:
        #name = str(name)
        name3 = name2.split()[0]
        if name == name3:
            group.append(name2)
    groups.append(group)

#print groups

for i in groups:
    print(i)

