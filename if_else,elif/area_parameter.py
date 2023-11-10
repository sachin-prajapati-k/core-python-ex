lenth=int(input("enter the lenth"))
height=int(input("enter the height"))
if lenth==height:
    print("this is a square")
    print('''want to check area or parameter?
y/n''')
    ans=input()
    if ans=='y':
        print('''press a for area
press p for parameter''')
        ch1=input()
        if ch1=='a':
            print("area of square is= ",lenth*lenth)
        if ch1=='p':
            print("parameter of square is= ",lenth*4)
        else:
            print("have a good day")
    else:
        print("have a good day")
else:
    print("this is a rectangle")
    print('''want to check area or parameter
y/n''')
    ans=input()
    if ans=='y':
        print('''a for area
p for parameter''')
        ch=input()
        if ch=='a':
            print("the area of rectangle =",lenth*height)
        if ch=='p':
            print("the parameter of  rectangle =",2(lenth+height))
        else:
            print("have a good day")
