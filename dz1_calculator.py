#encoding:utf-8
import math

action = input('Введите действие над числами. Возможны:' + '\n' +
'сложение (+)' + '\n' +
'вычетание (-)' + '\n' +
'умножение()' + '\n' +
'деление (/)' + '\n' +
'квадратный корень (sqrt)' + '\n' +
'степень (**)' + '\n' +
'факториал(!)' + '\n' +
'логарифм (log)'+ '\n' +
'косинус (cos)'+ '\n' +
'синус (sin)')

if action == '+':
    number1 = float(input('Введите первое число:'))
    number2 = float(input('Введите второе число:'))
    result = number1 + number2
    print(result)

elif action == '-':
    number1 = float(input('Введите первое число:'))
    number2 = float(input('Введите второе число:'))
    result = number1 - number2
    print(result)

elif action == '**':
    number1 = float(input('Введите первое число:'))
    number2 = float(input('Введите второе число:'))
    result = number1 ** number2
    print(result)

elif action == '/':
    number1 = float(input('Введите первое число:'))
    number2 = float(input('Введите второе число:'))
    result = number1 / number2
    print(result)

elif action == '*':
    number1 = float(input('Введите число:'))
    number2 = float(input('Введите степень:'))
    result = number1 * number2
    print(result)

elif action == 'sqrt':
    number1 = float(input('Введите число:'))
    result = math.sqrt(number1)
    print(result)

elif action == '!':
    number1 = float(input('Введите число:'))
    result = math.factorial(number1)
    print(result)

elif action == 'log':
    number1 = float(input('Введите число:'))
    number2 = float(input('Введите основание логарифма:'))
    result = math.log(number1,number2)
    print(result)

elif action == 'sin':
    number1 = float(input('Введите число:'))
    result = math.sin(number1)
    print(result)

elif action == 'cos':
    number1 = float(input('Введите число:'))
    result = math.cos(number1)
    print(result)

else:
    print('Не знаю, что ты от меня хочешь:)')