#!/opt/local/bin/python 

def square(x):
    '''
    Calculate the area for a square with of width = x
    '''
    return x**2

def circle(r):
    '''
    Calculates the area of a circle of radius r
    '''
    pi = 3.14159
    return pi * r**2

#print('The square of 4 is ', square(4))

shape = input('For which shape do you want the area? (square/circle) ')
if shape == 'square':
    x = input('Lenght size?')
    print('Area = %.2f' %square(float(x)))


if shape == 'circle':
    x = input('Radius length?')
    print('Area = %.2f' %circle(float(x)))

elif (shape != 'square') & (shape != 'circle'):
    print('I do not know that shape')

