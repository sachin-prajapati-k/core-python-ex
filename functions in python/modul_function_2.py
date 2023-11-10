#we can import all functions from module like this
# also ''' from <module name> import <function name> 
import module_21 as mod
print(mod.sum(3,4))
print(mod.mul(2,5))

#we can also use this mehode to import a function according to our need
# "*" is used to import all functions
from module_21 import *
print(sum(10,20))

print(mul(5,6))
