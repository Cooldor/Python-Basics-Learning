print("before the function")


def show():
    print("Function")


print("after function")


show()

print("after function")

show()


def show2():
    x = 7
    return x


y = show2()

z = show2() + 10
print(y)
print(z)

print(show2())
print(show())

# if define z variable below(after) function start , function won't see it (will be error)


def show3():
    x = 7 + z
    return x


print(show3())

z = 9

print(show3())


print("Functions")


def say_greetings():
    print("Welcome to the home")


print("Upper")
say_greetings()
print("Down")


def say_greetings(name, time, number):
    print("Welcome to the home, " + name + ", you are" + time + str(number))


say_greetings("Floppa", "you are on time ", 7)
say_greetings("Donald", "you are late ", 9)


print("Return Statement")


def cube(num):
    num*num*num


print(cube(3))


def cube(num):
    return num*num*num


print(cube(5))


def cube(num):
    return num*num*num
    print("No pass here")


result = cube(4)
print(result)


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(605, 4, 45))

print("!= means not equal")


j = [9, 8, 7, 6]

# count = 0
# for i in j:
#     count += 1
# print(count)


def count_list(par):   # parameter
    count = 0
    for _ in par:
        count += 1
    return count


print(count_list(j))    # argument


h = ["a", "a", "h"]
print(count_list(h))

k = [9, 8, 7, 5, 7, 5]
print(count_list(k))


def count_list(par, count=0):   # parameter #count

    for _ in par:
        count += 1
    return count


print(count_list(j, -1))   # counting the range of list or index of last element


def count_list(par, par2=False, count=0):   # parameter
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ

    else:
        for _ in par:
            count += 1
        return count


j = [9, 8, 7, 6]

print(count_list(j, True, -1))

h, p = count_list(j, True)

print(h)
print(p)


def name(u, g, *args, key):
    print(u)
    print(g)
    print(args)
    print(key)


name(7, 8, 9, 10, 11, key=12)


def exclusive_item(*args, key=False):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key is True:
        new_list.sort()
    return new_list


z = [9, 8, 7]
x = [8, 8, 9, 7, 6, 5]
c = [1, 2, 3, 4, 5, 6, 7, 7]

t = exclusive_item(z, x, c, key=True)
print(t)


x = 5  # global oblast vidimosti


def name():
    a = 10          # local oblast vidimosti (Peredat v global mozno c pomoIIIIo return(Peredaet ne peremennie a zna4enie kotoroe v neu codezitc9))
    print(x)
    return a


# print(a) Error

h = name()
print(h)

x = 5


def name():
    x = 10
    print(x)


print(x)


x = 5


def name():
    x = 10
    print(x)

print(x)
name()



x = 5


def name():
    global x
    x = 100
    print(x)


name()
print(x)


def name():
    x = 100
    return name2(x)


def name2(par):
    print(par)


name()


x = 5


def name():
    x = 10
    def name2():
                                 # nonlocal x
        x = 100
        print(x)
    name2()
    print(x)


name()
print(x)


import math

PI = math.pi


def radius():
    n = float(input("Diameter of the Cylinder (cm): "))
    n = n / 2
    return n


def height():
    m = float(input("height of the cylinder (cm): "))
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
