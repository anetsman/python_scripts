#!/usr/bin/python3

num = 2
while num < 100:
	value = 2
	is_prime = True
	for value in range (2, num):
		if num % value == 0:
			is_prime = False
			break
	if is_prime:
		print(num, end=' ')
	num += 1