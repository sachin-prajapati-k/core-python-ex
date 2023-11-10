#python has inbuilt random module
#random have three methods
import random as r
'''
    random 'randint()' method
    returns a number between x and y (both included):
    '''
print("randint method")
print(r.randint(2,8))

'''
    random 'randrange()' method
    returns a number between 3(included) and 9 (not included):
    '''
print("randrange method")
print(r.randrange(2,9))

'''
    random 'choice()' method
    returns a random element from a list:
    '''
print("choice method")
l=["apple",34,"mango","banana"]
print(r.choice(l))

#other random functions
a=r.random()
print(a)
'''
    'random' function it returns a random float number between
    0 and 1.
    '''
#shuffle function
'''
    takes a sequence and returns the sequence in a random order.
    '''
r.shuffle(l)
print(l)
#uniform function
'''
    returns a random float number between two given parameters
    '''
m=r.uniform(2,7)
print(m)


















