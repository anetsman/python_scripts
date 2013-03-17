#!/usr/bin/python3

v1 = eval(input("enter first number: "))
v2 = eval(input("enter second number: "))
if v1 > v2:
	mi = v2
	ma = v1
else:
	mi = v1
	ma = v2
v3 = int(input("enter third number: "))
if mi > v3:
	mi = v3
elif ma < v3:
	ma = v3
v4 = eval(input("enter fourth number: "))
if mi > v4:
	mi = v4
elif ma < v4:
	ma = v4
v5 = eval(input("enter fifth number: "))
if mi > v5:
	mi = v5
elif ma < v5:
	ma = v5
print(mi, ma)