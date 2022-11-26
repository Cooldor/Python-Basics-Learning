d1 = {"a": 7}
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
print(d3)
d3 = dict.fromkeys([1, 2, 3, 4, 5], "value")
print(d3)

# Dicts methods
# clear method for clear the dict
d5 = d1.copy()
print(d5)
print(d1.items())     # return dict to Lists in tuple (for cycles "for")
print(d1.keys)        # return keys from dicts in Lists (for cycles "for")
print(d1.values())    # return values from dicts in Lists (for cycles "for")
d1.update(d2)         # add all keys + values from one dict into another one
t = d1.pop("a")       # not only deletes specific pair of key + value but also returns the value into the variable
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


def buy():                              # shopping function for 37-th string
    pay = 0
    while True:
        enter = input("What to buy?\n")
        if enter == "end":
            break
        pay += price[enter]
    return pay


print(users["Alex7"]["password"])
print(buy())
