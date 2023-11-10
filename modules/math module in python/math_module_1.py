import math as m
#math 'ceil' function
'''
    return the ceiling of 'x', the smallest integer greater than or equal to 'x'
    if 'x' is not a float, delegates to x.__ceil__(), which should return a integer
    value
    '''
x=15.4
print(m.ceil(x))
#math 'floor' function
'''
    return the floor of 'x', the largest integer smaller than or equal to 'x'
    if 'x' is not a float, delegates to x.__floor__(), which should return a
    integer value
    '''
j=9.1
print(m.floor(j))

#math 'fabs' function
'''
    return the absolute(positive) value of 'x'
    if we passes positive value it does not return any error
    '''
y=-22
print(m.fabs(y))

#math 'factorial' function
'''
    it returns the factorial of givin value of 'x'
    '''
z=5
print(m.factorial(z))

#math 'fsum' function
'''
    return a accurate floating point sum of values in the iterable
    '''
l=[10,20,30,50]
print(m.fsum(l))

#math 'sqrt' function
'''
    return square root of 'x'
    '''
k=144
print(m.sqrt(k))

























