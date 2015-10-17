#encoding:utf-8

import math

def circle_square(diametr):
    square = float(diametr*2)*math.pi/4
    return square

diametrs = (45, 338,19)
squares = ''
for i in diametrs:
    sq = circle_square(i)
    squares = str(sq) + ' ' + squares

difference = float(squares.split(' ')[1]) - float(squares.split(' ')[0])

print(difference)