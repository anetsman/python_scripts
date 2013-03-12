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
	return li
li = mc()
listm = []
print(li)

#li.sort()
min = li[0]
max = li[0]

for i in li:
	if i <= min:
		min = i
		listm.insert(0, i)
	elif i > max:
		max = i
		listm.append(i) 
		print(listm)
	else:
		maxx = len(listm)
		for c in listm:
			if c < maxx:
				listm.insert(listm.index(c), i)
print(listm)
