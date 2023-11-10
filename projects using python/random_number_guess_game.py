import random as rd
while True:
    cnum=rd.randrange(1,101)
    unum=int(input("enter your number"))
    if cnum>unum:
        print("computer number",cnum)
        print("your guess number is too low from computer")
    elif cnum<unum:
        print("computer number",cnum)
        print("your guess number is too high from computer")
    else:
        print("computer number",cnum)
        print("your guess number is equal to computer")
