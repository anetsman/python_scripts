#!/usr/bin/python3
from random import randrange

def mc():
        matrix = []
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
                matrix += [l]
        print(matrix)
#       def dlist():
#               return [li[i:i + row]] for i in range (0, len(li), row)
#       li = dlist()
#       for i in range (0, len(li), row):
#               li = [li[i:i + row]]
        return matrix
matrix = mc()
for i in matrix:
	i.sort()
	while i < len(matrix):
		for j in i:
			min = matrix [0][0]
			
#k = 0
#n = 1
#while n < len(matrix):
#        while k < (len(matrix)-n):
#                if matrix[k] > matrix[k+1]:
#                        matrix[k], matrix[k+1] = matrix[k+1], matrix[k]
#                k += 1
#        k = 0
#        n += 1
print(matrix)
