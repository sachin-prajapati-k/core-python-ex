#some functions of set
'''
    'set' this function converts a list into a set
    'add' this function add a new element
    'pop' this function removes the element randomly
    'remove' this function removes the element
    'clear' this function clear the set and return the 'set()'
    'discard' this function also removes the element
    'update' this function is also add the new value
    '''
l=[10,20,30,40,50]
print(type(l))
print(l)

s=set(l)
print(s)
'''
    it converts list into a set
    '''
s.add(11)
print(s)
'''
    it adds a new element in random position
    '''

s.pop()
print(s)
'''
    it removes the any value from the set
    '''
s.remove(10)
print(s)
'''
    it removes the givin value
    if item to be removed does not exist, remove() raise an error
    '''
s.discard(30)
print(s)
'''
    it also revoes the givin value
    if item to be removed does not exist, discard() does not raise any error
    '''
s.clear()
print(s)
'''
    it clear the all values and returns the set()
    '''
lst=[11,22,33,44]
s.update(lst)
print(s)













