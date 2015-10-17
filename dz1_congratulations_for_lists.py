#encoding:utf-8

a = [1, -20, 38, 0, 44]
b = [88, -20, 48, 4, 33, 2]

len_a = len(a)
len_b = len(b)

minimum = min(len_a, len_b)

for i in range(0, minimum):
    winner = min(a[i], b[i])

#* ... а далее пробежаться новым циклом по списку победителю по этой цифре столько элементов, сколько эта разница, и вывести на экран получившийся элемент.
    if abs(a[i]-b[i]) < 15:
        modul = abs(a[i]-b[i])
        print('Модуль разности равен: ' + str(modul) + ' Поздравляю!')
        if a[i] == winner:
            index = a.index(winner)
            if index+modul > len_a:
                modul_index = int(modul%len_a)
                index = index + modul_index
                if index <= len_a:
                    print('Число, равное модулю по своему индексу, начиная с числа победителя: ' + str(a[index]))
                else:
                    print('Число, равное модулю по своему индексу, начиная с числа победителя: ' + str(a[index-len_a]))
            else:
                    print('Число, равное модулю по своему индексу, начиная с числа победителя: ' + str(a[index+modul]))
        else:
            index = b.index(winner)
            if index+modul > len_b:
                modul_index = int(modul%len_b)
                index = index + modul_index
                if index <= len_b:
                    print('Число, равное модулю по своему индексу, начиная с числа победителя: ' + str(b[index]))
                else:
                    print('Число, равное модулю по своему индексу, начиная с числа победителя: ' + str(b[index-len_b]))
            else:
                    print('Число, равное модулю по своему индексу, начиная с числа победителя: ' + str(a[index+modul]))
