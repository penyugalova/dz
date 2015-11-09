# encoding: utf-8

#№8. Создаем программу-модуль "Жизнь на ферме" с набором классов:
#№9. абстрактные классы



#1. добавляем в ферму абстрактный класс - от 1 до 3.
# Добавила абстрактный класс животное

from abc import ABCMeta, abstractmethod
import random

class AbsAnimal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, *args):
        pass

#- бежать
    @abstractmethod
    def run(self):
        pass
#- голос
    @abstractmethod
    def voice(self):
        pass

#- продукт
    @abstractmethod
    def product(self):
        pass

#метод месяц у животных
    @abstractmethod
    def month(self):
        pass


#Все эти классы отнаследованы от базового "Животное".
class Animal(AbsAnimal):

    def __init__(self, x, y, z):

        self.speed        = x
        self.sound        = y
        self.productivity = z
        self.number       = random.randint(1,10)

    def run(self):
        self.distance = self.speed*self.number
        return self.distance

    def voice(self):
        self.shouts = self.sound*self.number
        return self.shouts

    def product(self):
        self.products = self.productivity*self.number
        return self.products

#- Утка
class Utka(Animal):

    def month(self):
        q = random.randint(0, 10)
        if q < 6:
            self.x = self.run()*q
            self.y = self.voice()*q
            self.z = self.product()
        else:
            self.x = self.run()
            self.y = self.voice()
            self.z = self.product()

        self.result = (self.x, self.y, self.z)
        return self.result

#- Собака
class Dog(Animal):

    def month(self):
        q = random.randint(10, 50)
        if q < 30:
            self.x = self.run()*q
            self.y = self.voice()*q
            self.z = self.product()
        else:
            self.x = self.run()
            self.y = self.voice()
            self.z = self.product()

        self.result = (self.x, self.y, self.z)
        return self.result

#- Корова
class Cow(Animal):

#Там циклом проходим по всем животным, запуская их собственный метод "прошелМесяц" (какое животное сколько раз делает продукт, как успешно, где использовать random, какие случайные факторы внести в жизнь фермы, решайте сами).
    def month(self):
#элемент рандома
        q = random.randint(0, 15)
        if q < 10:
            self.x = self.run()*q
            self.y = self.voice()*q
            self.z = self.product()
        else:
            self.x = self.run()
            self.y = self.voice()
            self.z = self.product()

        self.result = (self.x, self.y, self.z)
        return self.result

#2. Также нужен класс Ферма.

class Ferma:

    def __init__(self, x, y, z):
        self.n_utka, self.n_dog, self.n_cow = x, y, z
        self.n_animals = (self.n_utka, self.n_dog, self.n_cow)
        self.utki   = []
        self.dogs   = []
        self.cows   = []

        self.r_utka = []
        self.r_dog  = []
        self.r_cow  = []

        self.utka_run           = int()
        self.utka_voice         = int()
        self.utka_productivity  = int()

        self.dog_run            = int()
        self.dog_voice          = int()
        self.dog_productivity   = int()


        self.cow_run            = int()
        self.cow_voice          = int()
        self.cow_productivity   = int()

#Программа инициализирует ферму с заданным числом каждого животного.
    def create(self, *args):
        for k, i in enumerate(self.n_animals):
            for ii in range(0, i):
                if k == 0:
                    self.utki.append(Utka(10, 50, 10))
                elif k == 1:
                    self.dogs.append(Dog(40, 500, 0))
                else:
                    self.cows.append(Cow(2, 10, 400))
        self.animals = (self.utki, self.dogs, self.cows)
        return self.utki, self.dogs, self.cows, self.animals

#Далее запускается метод класса Ферма "прошелМесяц".
#Далее запускается метод класса Ферма "своднаяИнформация", который расскажет нам об изменениях на ферме.

    def month(self):

        for k, animal in enumerate(self.animals):
            for i in animal:
                if k == 0:
                    self.r_utka.append(i.month())
                elif k == 1:
                    self.r_dog.append(i.month())
                else:
                    self.r_cow.append(i.month())

#Далее запускается метод класса Ферма "своднаяИнформация", который расскажет нам об изменениях на ферме.
#Оказалось удобнее сделать все же не отдельным методом, а частью метода "прошел месяц". Лаконично вписывается.

            for i in self.r_utka:
                self.utka_run           += i[0]
                self.utka_voice         += i[1]
                self.utka_productivity  += i[2]

            for i in self.r_dog:
                self.dog_run            += i[0]
                self.dog_voice          += i[1]
                self.dog_productivity   += i[2]

            for i in self.r_cow:
                self.cow_run            += i[0]
                self.cow_voice          += i[1]
                self.cow_productivity   += i[2]

        print('Утки за месяц набегали - ' + str(self.utka_run) + ', накричали - ' + str(self.utka_voice) + ', дали яиц ' + str(self.utka_productivity))
        print('Собаки за месяц набегали - ' + str(self.dog_run) + ', накричали - ' + str(self.dog_voice) + ', произвели пользы ' + str(self.dog_productivity))
        print('Коровы за месяц набегали - ' + str(self.cow_run) + ', накричали - ' + str(self.cow_voice) + ', дали молока в литрах ' + str(self.cow_productivity))

#последовательность животных строгая: утки, собаки, коровы
ferms = Ferma(3, 4, 6)

ferms.create()
ferms.month()