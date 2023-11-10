#python have 2 types of function
'''
    1. pre defined function or built in function i.e. sum,max,len etc.
    2. user defined function i.e. we can make function
    '''
#there are 3 type of user defined function
''' "simple function" '''
def simplefn():
    print("sachin prajapati")
'''
    but this function does not print anything
    we have to call the function to print
    '''
simplefn()

''' "function with arguments" '''
def add(a,b):
    print(a+b)
add(12,12)

def sums(m,n):
    print(m+n)
x=10
y=20
sums(x,y)

''' "return type" '''
def mul(j,k):
    m=j*k
    return m
multiply=mul(2,5)
print(multiply)
    
