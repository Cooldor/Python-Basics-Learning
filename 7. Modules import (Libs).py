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

from dis import dis

# lambda function
# simple function:


def some(o):
    return o / 5


# lambda function:


var = lambda x: x / 5      # different syntax that takes less place in the program

print(some(7))
print(var(7))

print(dis(some))
print(dis(var))

# Another example:

list_of = [['Adam', 29], ['Jonny', 3*1/12], ['Jess', 25]]


def s(x):
    return x[1]


r = sorted(list_of, key=s)   # function (sorted) sorting all the list ,
print(r)                     # for sorting needed the name of the list(variable)
#                            # and the key parameter (function name that will process the result

r = sorted(list_of, key=lambda x: x[1])   # lambda takes less place
print(r)

x = list(filter(lambda x: x[1] > 18, list_of))  # function (filter) used to create a new list by excluding some values
print(x)  # it checks the condition of boolean value in the first parameter(True or False), second is a list for check

