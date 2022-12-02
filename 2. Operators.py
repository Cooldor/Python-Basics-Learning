print("Operators")
# Booleans
is_visible = True
is_handy = True

if is_visible and is_handy:
    print("I saw you and I can prove that you are handy")
elif is_visible and not is_handy:
    print("I saw you, but you wasn't helpful")
elif not is_visible and is_handy:
    print("I didn't see you, but it looks like you were handy")
else:
    print("I didn't see you and it looks like you weren't handy")

x = 0

if x == 0:
    print("if")
elif x > 0:
    print('elif')
else:
    print('else')

x = 3

if x == 0:
    print("if")
elif x > 0:
    print('elif')
else:
    print('else')

x = -5

if x == 0:
    print("if")
elif x > 0:
    print('elif')
else:
    print('else')
...

x = 5

if x == 0:
    x += 1
print(5 / x)

x = -5

if x == -5:
    x += 1
print(5 / x)

x = 0

if x == 0:
    x += 1
print(5 / x)

...

x = 0

if x == 0:
    x = 1
    print("x was equal to 0")

elif type(x) is type(5) or type(x) is type(5.5):
    print("x is a valid number")

else:
    print("X is not a valid number")
    x = 1

print(100 / x)

x = 5

if x == 0:
    x = 1
    print("x was equal to 0")

elif type(x) == type(5) or type(x) == type(5.5):
    print("x is a valid number")

else:
    print("X is not a valid number")
    x = 1

print(100 / x)

x = [2, 4]

if x == 0:
    x = 1
    print("x was equal to 0")

elif type(x) == type(5) or type(x) == type(5.5):
    print("x is a valid number")

else:
    print("X is not a valid number")
    x = 1

print(100 / x)

...
# Cycles (loops)

x = 0

while x < 5:
    x += 1
    print(x)

else:
    print(x)

print(x)

x = int(input())

count = 0
y = 1

# Factorial cycle
while count < x:
    count = count + 1
    y = count * y

else:
    print(y)

x = ""

while len(x) < 5:
    y = input(" Enter your number: ")

    x += y

else:
    print(x)

x = ""

while len(x) < 5:
    y = input(" Enter your letter: ")
    if y == "o":
        continue
    if y == "l":
        break
    x += y

else:
    print(x)

print("Program is continue to work")

m = "string or Article"
count = 0
for I in m:
    if I == "t":
        print("Letter t is in the string")
        count += 1
    if I == "a":
        break           # not breaking the program with capital "A" , clarification needed for capital letters
else:
    print("Cycle completed, letters t", count)

print(" Program is continue to work")

x = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"      # letters counting program in the random string
y = input("Enter the string:\n")

for i in x:
    count = 0
    for r in y:                                                 # nested loop(cycle into the cycle)
        if i == r:
            count += 1
    if count > 0:
        print("Letters", i, "Were", count)

...

for x in range(10):
    print(x)

for x in range(5, 10):
    print(x)

# steps

for x in range(5, 10, 2):
    print(x)

for x in range(10, -10, -2):
    print(x)

...
