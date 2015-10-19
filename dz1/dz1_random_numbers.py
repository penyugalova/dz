#encoding:utf-8

import random

nums = random.randrange(10)
nums = str(nums)

def random_list(number_of_elements):
    numbers = str(nums)
    for i in range(1, number_of_elements):
        number = random.randrange(10)
        numbers = numbers + '\n' + str(number)
    return numbers

result = random_list(5)
print(result)

file = open('random.txt', 'w')
file.write(result)
file.close()

file = open('random.txt', 'r')
value = file.read()
file.close()

import math

number1 = int(value[0])
number2 = int(value[2])
number3 = int(value[4])
number4 = int(value[6])
number5 = int(value[8])

sum_of_two = number1 + number2

power_sqrt = math.sqrt(number3*number4)

print('Сумма первых двух чисел равна: ' + str(sum_of_two) + '\n' + 'Квадрат из перемноженных третьего и четвертого числа равен: ' + str(power_sqrt))

print('Максимальное из этих вух число: ' + str(max(sum_of_two, power_sqrt)))

cosinus = math.cos(number5)