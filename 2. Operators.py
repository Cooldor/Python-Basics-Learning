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
# While and for loops have same (else:) default operator

x = 0               # loop while works as long as condition TRUE

while x < 5:        # If there is no condition it can run indefinitely (this MUST be avoided)
    x += 1
    print(x)

else:        # else operator is not required (not must have) in the loop, it is executed after the loop is completed
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
count = 0     # for loop (I) - variable in which specifies the element of sequence
for I in m:   # and in (m) variable the sequence we want to iterate
    if I == "t":
        print("Letter t is in the string")
        count += 1
    if I == "a":
        break           # not breaking the program with capital "A" , clarification needed for capital letters
else:
    print("Cycle completed, letters t", count)

print(" Program is continue to work")


number_grid = [             # nested loop + 2D-list
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0])
print(number_grid[2][2])

for row in number_grid:
    # print(row) / will print 4  elements (lists) nested into one big list
    for col in row:
        print(col)

x = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"      # letters counting program in the random string
y = input("Enter the string:\n")

for i in x:
    count = 0
    for r in y:                                                 # nested loop
        if i == r:
            count += 1
    if count > 0:         # without this (if) check in the end it will show ALL letters values from (x) variable
        print("Letters", i, "Were", count)

...

# func range

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
