#!/usr/bin/python3

from math import sqrt, pow

side1 = eval(input("Enter the lengthe of one side of triangel: "))
side2 = eval(input("Enter the second side of triangle: "))
hypotenuse = sqrt(pow(side1,2) + pow(side2,2))
print('hypotenuse is ', hypotenuse)