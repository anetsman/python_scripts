#! c:\Python33\python

value = eval(input("please enter number in a range 0...5: "))
if value < 0:
    print("Too small")
elif value == 1:
    print("one")
elif value == 0:
    print("zero")
elif value == 2:
    print("two")
elif value == 3:
    print("three")
elif value == 4:
    print("four")
elif value == 5:
    print("five")
elif value > 5:
    print("too large")
print("the end")
