#!/usr/bin/python3

from random import randrange

def mc():
	li = []
	column = eval(input("enter number of columns: "))
	row = eval(input("enter number of rows: "))
	for c in range (1, row + 1):
		l = list()
		a = 0
		while a < column:
			b = randrange(1, 1000)
			l += [b]
			a += 1
		print(l)
		li += l
	print(li)	
	k = 0
	n = 1
	while n < len(li):
		while k < (len(li)-n):
			if li[k] > li[k+1]:
				li[k], li[k+1] = li[k+1], li[k]
			k += 1
		k = 0
		n += 1
	def dlist():
		return [li[i:i + row] for i in range (0, len(li), row)
	li = dlist()
	return li
li = mc()
print(li)

