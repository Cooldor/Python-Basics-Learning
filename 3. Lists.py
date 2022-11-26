print("Lists")
if __name__ == "__main__":

    def some_function():
        print("Main module")


some_function()

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


x = [9, 8, 7, 6, 5]
x.append(4)
x.insert(1, 7)
x.clear()
x.extend(["a", "b"])
h = x.copy()
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

# синтаксис срезов [start:stop:step]


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

for i in range(len(x)):
    y.append(x[i] + 3)
print(x)
print(y)


t = list(x)
t[0] = 10
x = tuple(t)
print(x)
#  z, c, b = x

r = 5
u = 7

r, u = u, r

print(x[1:5])

x = (9, 8, 7, 6, 5, 4, 3, 9, 9)
print(x.count(9))

x = (9, 8, 7, 6, 5, 4, 3)
print(x.index(9))

h = (1, 2, 3)
h += (4, 5)
print(h)


h = (1, 2, 3)
h += (4, 5)
g = h
print(h)
print(g)
