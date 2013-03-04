#!/usr/bin/python3

all = 0
sum = 0
while all <= 10: 
	num = eval(input("Enter the float-point number: "))
	sum += num
	if all == 0:
		min = num
		max = num
	else:
		if min > num:
			min = num
		elif max < num:
			max = num
	all += 1
	average = sum/all			
print(sum, max, min, average)
