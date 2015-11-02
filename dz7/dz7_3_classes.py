# encoding: utf-8
__author__ = 'Liubov Penyugalova'

#создаем 3 отдельных класса со следующими атрибутами

#Танк (модель=строка, шасси=False/True, скорость=число, гусеницы=False/True)
class Tank:


    def __init__(self):
        self.shassi      = True
        self.speed       = 40
        self.track_shoe  = True


    def model(self, model='T34'):
        self.model = model
        return self.model

#2. У каждого класса метод status, выводящий состояние объекта на данный момент.
    def status(self):
        if self.shassi == True and self.speed !=0 and self.track_shoe == True:
            print('Завелось, корыто, едем!')
        else:
            print('Увязли танки поуши в грязи! Не едет ничего, проверь характеристики')


#Машина (модель, колеса, скорость)
class Car:


    def __init__(self):
        self.wheels      = 4
        self.speed       = 60


    def model(self, model='Volvo'):
        self.model = model
        return model

#2. У каждого класса метод status, выводящий состояние объекта на данный момент.
    def status(self):
        if self.wheels == 4 and self.speed !=0:
            print('Погнали!')
        else:
            print('Не едет машина. Проверь характеристики.')

#Телега (колеса, скорость)
class Cart:

    def __init__(self):
        self.wheels      = 4
        self.speed       = 20

#2. У каждого класса метод status, выводящий состояние объекта на данный момент.
    def status(self):
        if self.wheels == 4 and self.speed !=0:
            print('Но! Поехали!')
        else:
            print('То ли я дурак, то ли телега не едет. Проверь характеристики.')



#3. Создаем и собираем сколько-то новых объектов этих классов в список cars.

a   = Tank()
a1  = Tank()
a2  = Tank()
b   = Car()
b1  = Car()
b2  = Car()
c   = Cart()
c1  = Cart()
c2  = Cart()

#4. Делаем несколько действий с этими объектами (Например, назначили машине "Audi" скорость 90, у танка 'Т34' сняли шасси).

a.track_shoe    = False
a1.speed        = 10
a2.shassi       = False

b.wheels        = 3
b1.speed        = 120
b1.model        = 'Audi'
b2.speed        = 90

c.speed         = 40
c1.wheels       = 2
c2.speed        = 50

#5. В конце программы выводим состояния всех объектов из cars.

cars = (a, a1, a2, b, b1, b2, c, c1, c2)

for machine in cars:
    machine.status()
