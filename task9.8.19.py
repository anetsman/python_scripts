#!/usr/bin/python3

list = []
llist = []
list = eval(input("enter the list: "))
num = eval(input("enter the number: "))

for i in list:
	if i > num:
		llist += [i]
llist.sort()
print(llist)