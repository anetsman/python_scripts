#!/usr/bin/python3

all = 0
sum = 0
if all == 0:
	num = eval(input("Enter the float-point number: "))
	min = num
	max = num
while all <= 10: 
	num = eval(input("Enter the float-point number: "))
	sum += num
	if min > num:
		min = num
	elif max < num:
		max = num
	all += 1
	average = sum/all		
print(sum, max, min, average)
