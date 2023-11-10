'''
    dictionary have some functions to access the the data
    '''
d={
    'name':"sagar prajapati",
    'age':23,
    'language':'python',
    'course':'ccc'
    }
a=d.get('age')
print(a)
'''
    'get' function is access the value by giving key
    we can also get the value by giving key in [] braces    '''

for i in d.keys():
    print(i)
'''
    'keys' function is access the all keys in the dictionary
    '''

for b in d.values():
    print(b)
'''
    'values' function is access the all values in the dictionary
    '''

for x,z in d.items():
    print(x," -",z)
'''
    'items' function is access the all keys and values in the dictionary
    for this function we have to take two parameters
    '''

del d['age']
print(d)
'''
    'del' is a keyword it removes the value through giving key
    '''
d.pop('name')
print(d)
'''
    'pop' keyword is also used for delete the value through giving key
    '''

di=dict(name='harsh',age=23,duration='3 month')
print(di)
'''
    'dict' keyword is used to create dictionary but we have to give a variable
    name and the data is stored by giving var and values which converted after
    key and values
    '''

di.update({'name':'sachin','age':20})
print(di)
'''
    this function is used to updata the value of a dictionary by using 'update'
    function by giving keys and values
    '''

di.clear()
print(di)
'''
    'clear' function is clear the compleste dictionary
    and returna a empty dictionary
    '''






































    
