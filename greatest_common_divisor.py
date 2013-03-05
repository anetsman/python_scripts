#!/usr/bin/python3

num1, num2 = eval(input("enter two numbers, which gcd needs to be found: "))
def gcd(num1, num2):
# Determine the smaller of num1 and num2
	min = num1 if num1 < num2 else num2
# 1 is definitely a common factor to all ints
	largestFactor = 1
	for i in range(1, min + 1):
		if num1 % i == 0 and num2 % i == 0:
			largestFactor = i # Found larger factor
			print(largestFactor)
	return largestFactor
gcd(num1, num2)