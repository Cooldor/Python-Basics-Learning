print("before the function")


def show():
    print("Function")


print("after function")


show()

print("after function")

show()


def show2():     # to continue to use values from the function in the program we needed return statement(operator)
    x = 7 + z    # it will return the value at the start point of the function
    return x                


z = 7
# if define "z" variable below(after) function start , function won't see it (will be error)

y = show2()
# Example : (z = 7 in this string) will not be defined by the function (show2)
z = show2() + 10
print(y)
print(z)
# z variable was changed so the value in the function too
print(show2())
print(show())


def show3():
    x = 7 + z
    return x


print(show3())

z = 9

print(show3())


def say_greetings():
    print("Welcome to the home")


print("Upper")
say_greetings()
print("Down")


def say_greetings(name, time, number):
    print("Welcome to the home, " + name + ", you are" + time + str(number))


say_greetings("Floppa", "you are on time ", 7)
say_greetings("Donald", "you are late ", 9)


def cube(num):                  # none because no return statement to return the value to the function
    num*num*num


print(cube(3))


def cube(num):              # cube function
    return num*num*num


print(cube(5))


def cube(num):
    return num*num*num
    print("No pass here")


result = cube(4)                # saved in the variable
print(result)


def max_num(num1, num2, num3):                  # max number function
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(4, 555, 45))

print("!= means not equal")


j = [9, 8, 7, 6]

# count = 0
# for i in j:
#     count += 1
# print(count)


def count_list(par):   # parameter is a random variable defined inside a function in the parentheses
    count = 0
    for _ in par:      # a function that calculates the length of a list
        count += 1
    return count


# Now this is generic function , now you can pass any values of variables in any sequence as an argument
print(count_list(j))    # argument needed (must have) if you have parameter in your function , otherwise - error


h = ["a", "a", "h"]
print(count_list(h))

k = [9, 8, 7, 5, 7, 5]
print(count_list(k))

print(count_list("string"))


def count_list(par, count=0):  # count is default (named) parameter because this variable already has the value

    for _ in par:
        count += 1             # the amount of parameters and the amount of arguments must always match (be same)
    return count               # on condition they are not default (parameters)


print(count_list(j, -1))
# if argument to this default parameter = 0 (empty or is not written) counting the range of the list
# if argument to this default parameter = -1 shows the index of the last element in the list


def count_list(par, par2=False, count=0):   # par normal(unnamed) parameter, par2 and count default parameters
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ

    else:
        for _ in par:
            count += 1
        return count


j = ["str", 8, 7, 6]

print(count_list(j, True, -1))

h, p = count_list(j, True)              # saved as variables

print(h)
print(p)

# parameter args (asterisk (*)) allows to pass a variable number(more than one) of arguments to a function
# for this parameter allows you to pack arguments into a tuple


def name(u, g, *args, key):         # after *args parameter comes key parameter
    print(u)
    print(g)
    print(args)
    print(key)


name(7, 8, 9, 10, 11, key=12)   # for key parameter, a value can only be assigned using a named argument
# otherwise all values will go to *args parameter + error


# A function that weeds out duplicate values from lists and generates a new list with unique non-repeating ones
# algorithm function


def exclusive_item(*args, key=False):
    new_list = []
    for i in args:                              # nested loop processing
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key is True:                             # without key parameter (True) will be not sorted list
        new_list.sort()
    return new_list


z = [9, 8, 7, 0, 0, 0]
x = [8, 8, 9, 7, 6, 5]
c = [1, 2, 3, 4, 5, 6, 7, 7]

t = exclusive_item(z, x, c, key=True)
print(t)


x = 5  # this is global scope


def name():
    a = 10          # this is local scope (inside the function)
    print(x)        # you can transfer it to global scope using the return statement
    return a        # NOT pass the variables from the local scope, but the values it CONTAINS


# print(a)  will be Error, because it cant pass variable (a) from local scope to global scope

h = name()   # saved as variable
print(h)


x = 5           # global


def name():
    x = 10      # local
    print(x)


name()                  # x variable changed in local scope
print(x)                # but x variable not changed in global scope


x = 5


def name():
    global x        # global gives the command that we want to change something in the global scope , not in local
    x = 100
    print(x)


name()
print(x)

x = 5


def name():
    x = 100
    return name2(x)             # passing values between the functions


def name2(par):
    print(par)


name()


x = 5


def name():
    x = 10
    def name2():            # function declared in function (nested function), we use nonlocal key word =>
        # nonlocal x        # if we do not want to create new local scope (in variable x) by this nested function
        x = 100             # each function has a separate local scope
        print(x)
    name2()
    print(x)


name()
print(x)

# Structured code using functions that calculates the volume/weight of cylinder
# usage of local scope in priority, it saves RAM (not take up space in memory like global) and easier to read
# example:

import math

PI = math.pi


def radius():
    n = float(input("Diameter of the Cylinder (cm): "))
    n = n / 2
    return n


def height():
    m = float(input("Height of the cylinder (cm): "))
    return m


def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s*h
    return v


# print("volume of cylinder", volume(), "cm3")


def weight(g):
    n = float(input("specific weight g/cm3: "))
    return g*n/1000


print("Weight of the cylinder (kg): ", weight(volume()))
# function (volume) is an argument to weight function ((g) parameter)
# that starts a chain of other functions work
