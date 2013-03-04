#! /usr/bin/python3

print("My computer doesn't work!")
print ("does it make some noise?")
choice = input("or show any lights? (y/n): ")
if choice == 'n': #have no power
    choice = input("Is it plugged in? (y/n): ") 
    if choice == 'n': #not plugged
        print('so plug it in!')
        print("if the problem persists, run the program again")
    else: #plugged
        choice = input("is the switch is the 'on' position? (y/n)")
        if choice == 'n': #not switched on
            print("turn it on!")
            print("if the problem persists, run the program again")
        else: #switched on
            choice = input("Does the comp have a fuse? (y/n)")
            if choice == 'n': #no fuse
                choice = input("isthe outlet ok? (y/n)")
                if choice == 'n': #fix outlet
                    print("check outlet circuit, or new outlet needed")
                    print("if the problem persists, run the program again")
                else:
                    print("call to support")
            else: #Check fuse
                print("check the fuse")
                print("if the problem persists, run the program again")
else: #comp has power
    print("call to support")  
