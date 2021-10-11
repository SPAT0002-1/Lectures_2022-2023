#!/opt/local/bin/python 

import sys

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

if len(sys.argv) == 1:
    print("Usage: %s shape_name value" % sys.argv[0])
    exit()

if sys.argv[1] == 'square':
    x = sys.argv[2]
    print('Area = %.2f' %square(float(x)))

if sys.argv[1] == 'circle':
    x = sys.argv[2]
    print('Area = %.2f' %circle(float(x)))

elif (sys.argv[1] != 'square') & (sys.argv[1] != 'circle'):
    print('I do not know that shape')

