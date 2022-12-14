import testlib          # importing specific module
# import testlib as t   # to shorten the name of module (t.k) for variable (k) 

# from testlib import *  # another option for importing modules which brings all objects from module into our scope
# means no need to access the module itself like (testlib.k2), you can directly work with objects from specific module

from testlib import k, raise_to_power  # same , but importing only specific objects from module to our scope , not all

# importing my own module  from this project for test (raise to power module) named testlib

print(dir())  # function dir shows available for work modules in the current file
print(help(testlib))


print(testlib.raise_to_power(4, 3))  # module works fine for (import testlib)
print(k)  # (from testlib import *)  the value of variable (k) already in this scope, so no need to write(testlib.k)
print(testlib.k)  # same , but for (import testlib), because importing the module itself

k = 12
print(k)
print(testlib.k)                        # did not change
print(testlib.__name__)                 # used __main__ module in testlib to not accept input function from this module
# for more info look into the testlib module
