#!/usr/bin/python3

from random import randrange

def mc():
	column = eval(input("enter number of counts: "))
	row = eval(input("enter number of rows: "))
	for c in range (1, row + 1):
		l = list()
		a = 0
		while a < column:
			b = randrange(1, 1000)
			l += [b]
			a += 1
		print(l)
		li = list()
		li += l
	return li
mc()
print(li)