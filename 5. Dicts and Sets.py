d1 = {"a": 7}       # the key in dicts can be any immutable data type (numbers (int, float), strings, tuples)
print(d1)
print(d1["a"])
d1["b"] = 9
print(d1)
d1["a"] = 8
print(d1)
del d1["a"]
print(d1)

d2 = dict(a=7)
print(d2)
d2 = dict([[1, 2], [3, 4], [5, 6]])
print(d2)

d3 = dict.fromkeys([1, 2, 3, 4, 5])
print(d3)       # [1, 2, 3, 4, 5] all are keys in this situation, and they do not have value (default value needed)
d3 = dict.fromkeys([1, 2, 3, 4, 5], "value")
print(d3)

# Dicts methods
# clear method for clear the dict
d5 = d1.copy()
print(d5)
print(d1.items())     # return dict to Lists in tuple (for loops "for")
print(d1.keys)        # return keys from dicts in Lists (for loops "for")
print(d1.values())    # return values from dicts in Lists (for loops "for")
d1.update(d2)         # add all keys + values from one dict into another one
t = d1.pop("b")       # not only deletes specific pair of key + value but also returns the value into the variable
print(t, d1)
if "c" in d1:         # alternative security check of the key existence using operators
    d1["c"]
y = d1.get("c", "not exists")   # for security check of the key existence + returns the value of the corresponding key into a variable
print(y)          # if it exists


price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

users = {
    "Alex7": {"password": 98854322, "id": 1957},
    "Jimmy66": {"password": 12345679, "id": 8732},
    "Bob33": {"password": 28652301, "id": 9921}
    }


# def buy():
#    pay = 0
#    while True:
#        enter = input("What to buy?\n")
#        if enter == "end":
#            break
#        pay += price[enter]
#    return pay


print(users["Alex7"]["password"])
# print(buy())


price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}
for i in price:
    print(i)

new_price = {}                                  # 15% discount new price

for i in price:
    new_price[i] = round(price[i] * 0.85, 2)    # round to round the value for specific (2) sign(number) after coma
print(price)
print(new_price)


for i in price.items():     # each object of (price) variable now in tuples
    print(i)

for key, value in price.items():  # each object of (price) variable now in separate variables (key and value)
    print(key)
    print(value)

new = {}                                    # reverse key to value
for key, value in price.items():
    new[value] = key
print(new)


for value in price.values():        # iterating a dictionary just over values
    print(value)


new_price = {}

for i in price.keys():                         # iterating a dictionary just over keys
    new_price[i] = round(price[i] * 0.85, 2)   # same as in string 64 but with better saving computing power
print(new_price)

# Sets
print("SETS")

t = {"a", "f", 1, 1, 2, (2, 5), 3}  # sets can consist of immutable data type (numbers (int, float), strings, tuples)
print(t)    # there are no indexes or keys in sets and any ordering (unordered collection of elements)
y = set()   # sets contains only unique elements (no duplicate elements)

# The essence o the sets ( For what they are needed):

x = (1, 2, 3, 4, 5, 6, 7)
y = [1, 2, 3, 4, 5, 6, 7]
u = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7}
h = {1, 2, 3, 4, 5, 6, 7}

print(x.__sizeof__())
print(y.__sizeof__())
print(u.__sizeof__())
print(h.__sizeof__())

# sets have the most size among all, but it is much faster works (transmits information, merging, etc) than others
import time


def exclusive_item(*args, key=False):
    new_list = []
    for i in args:                              # nested loop processing
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key is True:                             # without key parameter (True) will be not sorted list
        new_list.sort()
    return new_list


z = list(range(10000))
x = list(range(5000, 15000))
c = list(range(10000, 20000))

start = time.time()                 # checking time work between lists and sets
exclusive_item(z, x, c)
stop = time.time() - start          # it takes 18~ seconds on work with lists  with such values
print(stop)

start2 = time.time()
r = set(z)
t = r.union(set(x), set(c))         # union all variables with lists into one huge set
stop2 = time.time() - start2        # it takes 0.00500~ seconds on work with sets with such values
print(stop2)                        # sets are much faster than lists

# Sets Methods

z = {1, 2, 3, 4, 5}
x = {3, 4, 5, 6, 7}
z.add(6)      # adds an element to the set, if there is a duplicate element nothing will add
z.discard(6)  # deletes an element from the set, if there is no such element the error will not appear
z.remove(5)   # deletes an element from the set, if there is no such element the error will appear
y = z.union(x)  # unions sets + saved union sets into one variable
z.update(x)   # adds not same elements from another set to specified set
t = z.intersection(x)  # allows to define common (same, duplicate) elements
e = z.difference(x)  # shows which values from (z) set not found in set (x)

print(t)
print(y)
print(e)

# example of using sets:
# Need to do special big text parsing

new = set()

r = open("/Users/air/Desktop/text.txt")
new.update(set(r.read().split()))         # split str method that returns all words into a list
r.close()                                          # all backspace + comas and dots are gone

# comparing two texts

r = open("/Users/air/Desktop/text2.txt")
new.update(set(r.read().split()))
r.close()
print(new)


r = open("/Users/air/Desktop/text.txt")
r1 = set(r.read().split())
r.close()

# comparing two texts on duplicate elements(intersection)

r = open("/Users/air/Desktop/text2.txt")
r2 = set(r.read().split())
r.close()

new = r1.intersection(r2)
print(new)
# other method
new = r1.difference(r2)
print(new)
