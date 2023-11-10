print("calculation")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
choice=int(input("enter the value"))
if(choice==1):
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=a+b
    print("sum of the number",c)
elif(choice==2):
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=a-b
    print("substraction of the number",c)
elif(choice==3):
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=a*b
    print("multiplication of the number",c)
elif(choice==4):
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=a//b
    print("divide of the number",c)
else:
    print("invalid number")
