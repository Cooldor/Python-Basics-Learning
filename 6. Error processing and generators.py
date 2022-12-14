import os
# if user will enter not a number, but a letter, words, strings, etc for (enter) variable - error is inevitable
# using error processing operators to prevent an error from occurring
# also using while loop to repeat the loop until the user enters a suitable value

while True:
    try:                  # the section of code in which an error can occur is written in the block (try)
        enter = float(input("Enter a number: "))
        print(100/enter)
        break
    except ValueError:    # for the (except) operator need to clarify the type of error so that it intercepts it
        print("You enter not a number!")  # and after interception will reproduce the prepared code preventing the error
    except ZeroDivisionError:             # another possible error in this loop , so using except operator again
        print("Can't divide by zero!")
    else:                # operator (else) works only when there were not any errors in the (try) block
        print("Wow, You did great and and enter the correct value with the first attempt!")
    finally:             # the code written in finally operator works always (code is always executed)
        print("Will be working always!!")  # even if there was an error in (try) block ,
# even if there was an error in (try) block , the code from (finally) operator will be always executed

print("the program continues to work")


# context manager ( with , as)
# allows to work with resources that require closure in case of an error safely (saves data processed before the error)
# but can not do anything with error itself
with open("/Users/air/Desktop/ErrorTest.txt", "a") as r:   # (with) function (open) (as) variable r
    r.write("something" + "\n")                         # same as r = open("/Users/air/Desktop/ErrorTest.txt", "a")
#    10/0                             # random error
    r.write("something23")

print("continue to work")


# Generators of lists, dicts and sets
# the task to create new a list based on some other list
# using knowledge from past files its possible to do with (for) loop,
# but there is a way to make it easier with list generator
# example with (for) loop:

h = [9, 8, 7, 4, 5, 6, 3, 2, 1, 5, 5, -2]
new_h = []
for x in h:
    # if x % 2 == 0:      # that is how it looks like in loop (additional condition) for string 56
    new_h.append(x*2)
print(new_h)

# example with list, set, dict  generators
new_h2 = [x*2 for x in h]
z = {x*2 for x in h}
f = {x: x*2 for x in h}
print(new_h2)           # take up less space and works faster
print(z)
print(f)

g = [x for x in h if x % 2 == 0]       # how to write additional condition to generator
print(g)
print(type(g))

g = [x for x in h if x % 2 == 0 and x > 0]
print(g)

# nested loop in generator:

g = [os.path.join(z, i) for z, x, c in os.walk('/Users/air/Desktop/PycharmProjects') for i in c
     if '.txt in i']  # it is possible to move generator syntax to the next line
print(len(g))
print(g)
print(g.__sizeof__())

# One more example with generator for  selected loop

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)
print(new_price)

generator_style = {i: round(price[i] * 0.85, 2) for i in price.keys()}
print(generator_style)

# Generator expression

h = ['https:\\www.website.com', 'https:\\www.another_website.net',
     'https:\\www.this_website.com',
     'https:\\www.other_website.com',
     'https:\\www.mini_website.net', 'https:\\www.hidden_website.com']

n = [x.split('\\')[1] for x in h if '.com' in x]  # generator of list
print(n)
print(type(n))
print(n[1])

z = (x.split('\\')[1] for x in h if '.com' in x)      # generator expression
print(type(z))
print(z)                            # generate only one result (one element) per call unlike the list generator
# print(n[1])                       # will be error because there is no indexes in generator expressions
print(next(z))                      # (next) function shows what is the next element of iteration
print(next(z))
for i in z:
    print(i)

n = [x for x in os.walk('/Users/air/Desktop/Test Folder')]
print(n)
print(n.__sizeof__())
print("It was the list generator")


z = (x for x in os.walk('/Users/air/Desktop/Test Folder'))
print(next(z))
print(z.__sizeof__())
print("And that was the generator expression")

# generator function

# example of some specific function without generator function:


def some():
    list_text = []
    with open('text.txt', encoding='utf-8') as r:
        for x in r:
            list_text.append(x)
    return list_text


for i in some():
    print(i.split())

# Example of the same function but with generator function


def some_generator():
    with open('text.txt', encoding='utf-8') as a:
        for x in a:
            yield x         # operator (yield) works not same as (return), now it is the generator function


# this generator function saves more computer power than previous function
for i in some_generator():  # generator function will return one element for each iteration in this loop,
    print(i.split())          # while previous simple function returns all elements into the new list
# Result is the same


# one more example:

p = some_generator()         # same as generator expression
print(next(p))
print(next(p))
print(next(p))
for i in p:
    print(i)
