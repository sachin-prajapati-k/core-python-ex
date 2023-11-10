n1=int(input("enter the value 1 = "))
n2=int (input("enter the value 2= "))
op=input('''
add         +
substract   -
multiply    *
divide      /
enter the operator..''')
if op=='+':
     print("addition is = ",n1+n2)
elif op=='-':
    print("substraction is = ",n1-n2)
elif op=='*':
    print("multiplication is = ",n1*n2)
elif op=='/':
    print("divident is = ",n1/n2)
else:
    print("invalid operator.....")
