per=int(input("enter your percentage = "))
if per<=100:
    if per>80:
        print("A Grade")
    elif per>60:
        print("B Grade")
    elif per>50:
        print("C Grade")
    else:
        print("you are fail")
else:
    print("enter the correct percentage")
