print("Lists")

Food = ["Potatoes", "Mushrooms", "Beef"]
print(Food)

Food = ["Potatoes", "Mushrooms", "Beef"]
print(Food[1])
print(Food[-1])
print(Food[-2])

Food = ["Potatoes", "Mushrooms", "Beef", "Chicken", "Onion Rings"]
Food[1] = "Pizza"
print(Food[1:])
print(len(Food))

Food = ["Potatoes", "Mushrooms", "Beef", "Chicken", "Onion Rings"]
print(Food[1:3])

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray"]
Participants.extend(lucky_tickets)
print(Participants)

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray"]
Participants.append("Snowman")
print(Participants)

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray"]
Participants.insert(2, "Missed Sock")
print(Participants)

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray"]
Participants.remove("Bobby")
print(Participants)

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray"]
Participants.clear()
print(Participants)

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray"]
Participants.pop()
print(Participants)

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray"]
Participants.extend(lucky_tickets)
print(Participants)

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray"]

print(Participants.index("Kodo"))

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray", "Bobby"]
Participants.sort()
lucky_tickets.sort()
print(Participants.count("Bobby"))

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray", "Bobby"]
Participants.sort()
lucky_tickets.reverse()
print(Participants.count("Bobby"))

lucky_tickets = [5, 7, 12, 19, 25, 30]
Participants = ["Kodo", "Simple Stone", "Astaroth", "FacelessOne", "Bobby", "Stingray", "Bobby"]
Participants2 = Participants.copy()

print(Participants2)

m = [1, 2, 4, 6, "a", [1, 2], ["d", "f"]]
print(m[-1][0])
print(m)

m = [1, 2, 4, 6, "a", [1, 2], ["d", "f"]]
m[-2] = 7
print(m)

m[0] = m[0] + 2
print(m)

m = [1, 2, 4, 6, "a", [1, 2], ["d", "f"]]

m[1], m[2] = m[2], m[1]
print(m)

m = m + [7]
print(m)

m = [1, 2, 4, 6, "a", [1, 2], ["d", "f"]]

m = m*2
print(m)

n = list("string")
print(n)

n = list(range(10))
print(n)


n = list(range(10))

for i in n:
    print(i)

n = list(range(10))
m = []
for i in n:
    if i == 8:
        continue
    m += [i]
else:
    print(m)

# Lists methods
x = [9, 8, 7, 6, 5, 8]
x.append(4)             # adds element in the end of list
x.count(8)              # shows how many same elements in the list
x.reverse()             # flips the list
x.sort()                # sorts the list  in ascending order
x.pop(0)                # deletes element according to the specified index and can save it in the variable
x.remove(8)             # deletes specific element
x.insert(1, 7)          # adds element at the specified index in the list
x.clear()               # clears the list
x.extend(["a", "b"])    # extends in the end of list another list values
h = x.copy()            # copies list in the variable
print(x)
print(h)

n = list(range(10))
m = []
for i in n:
    if i == 8:
        continue
    m.append(i)
else:
    print(m)


n = list(range(1, 21))
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)

n = list(range(1, 21))
b = n
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
print(b)


n = list(range(1, 21))
b = n.copy()
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
print(b)

# syntax of slices [start:stop:step]


n = list(range(1, 21))
b = n[::]
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
print(b)


n = list(range(1, 21))
b = n[0::2]
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
print(b)


n = list(range(1, 21))
b = n[1::2]
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
print(b)


n = list(range(1, 21))
b = n[:5]
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
print(b)


n = list(range(1, 21))
b = n[5:]
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
print(b)


print("Tuples")
print("Tuples are immutable")

coordinates = (4, 5)
print(coordinates[1])

x = tuple("string")
print(x)

x = (9, 8, 7)
print(x[0] + 5)
print(x)

x = (9, 8, 7, 6, 5, 4, 3)

#  z, c, b = x

r = 5
u = 7

r, u = u, r

print(x[1:5])


x = [9, 8, 7, 6, 5, 4, 3]


for i in range(len(x)):
    x[i] += 3
print(x)
# impossible for tuples
#  z, c, b = x

r = 5
u = 7

r, u = u, r

print(x[1:5])


x = (9, 8, 7, 6, 5, 4, 3)
y = []
# possible for tuples
for i in range(len(x)):
    y.append(x[i] + 3)
print(x)
print(y)

# how to change the tuple
t = list(x)
t[0] = 10
x = tuple(t)
print(x)

# Tuples methods

x = (9, 8, 7, 6, 5, 4, 3, 9, 9)
print(x.count(9))                   # shows how many same elements in the tuple

x = (9, 8, 7, 6, 5, 4, 3)
print(x.index(9))                   # shows index of the element in the tuple

# It's possible to add in one tuple another one
h = (1, 2, 3)
h += (4, 5)
print(h)


h = (1, 2, 3)
g = h
h += (4, 5)

print(h)
print(g)
