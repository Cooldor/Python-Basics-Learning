print("The True Journey Starts Here")

print('VARIABLES + STRINGS')

character_name = "Poggo"
character_weight = "15 kg weight"
print("Once upon a time there was a doggo named " + character_name + ", ")
print(character_name + " was " + character_weight + ". ")
character_name = "Pogger"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_weight + " because he can't actually run. ")
Is_fat_doggo = True

# usage of escape sequence (str)
s = 'Let\'s \
write a \
string as "s" '
print(s)
print("D:\\path... ")
url = r"https:\www.youtube.com\new"  # (r) means only for read and all escape sequence will be ignored
url2 = "https:\\www.youtube.com\\new"  # or use backslash
print("interview\tbit")    # if needed to add  some space between words (tab space)
print("Interview \bBit")   # if needed to remove some space between words
print("cooldor\\'Gss")
print("Cooldor\nGSS")
print("Cooldor\"GSS")
print("Cooldor\GSS")

# String Methods

s = "string of text"

print(s[0:6])
print(s[3])
print("ing" in s)

# methods do not change the content of the original string

phrase = "cooldor GSS"
print(phrase + " is MVP")

phrase1 = "Cooldor GSS"
print(phrase1.lower())
print(phrase1)

phrase2 = "Cooldor GSS"
print(phrase2.upper())
print(phrase2)
phrase3 = (phrase2.upper())
print(phrase3)

phrase = "Cooldor GSS"
print(phrase.upper().isupper())

print(phrase.capitalize())   # first letter of string will be capital all others are lower
print(phrase)


phrase = "Cooldor GSS"
print(phrase.index("G"))

phrase = "Cooldor GSS"
print(phrase.replace("Cooldor", "Herba"))

path = "C:/Users/PyHS/Desktop/s.py"  # (/) linux path style need to change to windows path style (\) example:
path1 = path.replace("/", "\\")      # replaces specific elements
print(path1)

r = path1.split("\\")   # splits the string into a list by specific elements
print(r)
print(r[-1])

# we have a text, which need to be handled. Remove all brackets, quotes and line breaks. Example:

q = open("/Users/air/Desktop/text1.txt", encoding="utf-16")
r1 = q.read()
list_of_signs = ['(', ')', '"', "\n"]
for i in list_of_signs:
    r1 = r1.replace(i, "")
print(r1)

r2 = r1.split()
print(r2)

new_text = "_".join(r2)  # adds the selected object to related elements in the variable
print(new_text)

# f-strings
# in f-strings are possible to get results from actions with expressions, variables into the string itself
enter = input("Your name: ")
var = "string"

s2 = f"Hello {enter}, I can do it in f-string {len(var)} or {4 + 4} , enjoy!"   # (f) for f-string creation
print(s2)

print("Numbers")

print(9 * (8 + 5))
print(11 % 3)

number = 9
number2 = 10
result = number + number2
print(result)

number = 25
number2 = 67
number3 = 59
result = number * number2 * number3
print(result)

num1 = num2 = 7
print(num1, num2)

num_1, num_2 = 8, 7
print(num_1, num_2)

swap1 = 4
swap2 = 1
swap1, swap2 = swap2, swap1
print(swap1, swap2)

swap1 = 4
swap2 = 1
swap1, swap2 = swap2, swap1 + swap2
print(swap1, swap2)

swap2 = swap2 - number
print(swap2, number)

swap2 -= number
print(swap2)

my_num = -8
print(abs(my_num))

my_num = -8
print(pow(6, 7))
print(max(6, 7))
print(min(6, 7))
print(round(4.5))

from math import *
print(floor(4.6))
print(ceil(4.6))
print(sqrt(49))

z, x, c = [1, 2, 3]
print(z)
print(x)
print(c)

z, *x, c = [1, 2, 3, 4, 5]
print(z)
print(x)
print(c)

print('Types of Data')

a = None
print(type(a))
a = 1
print(type(a))
a = 1.0
print(type(a))
a = 1 + 1j
print(type(a))
a = '1'
print(type(a))
a = [1, 1, 'a']
print(type(a))
a = (1, 1, 'a')
print(type(a))
a = {1, 2, 'a'}
print(type(a))
a = {'a': 1, 'b': 2}
print(type(a))
a = True
print(type(a))

name = input("Enter your name: ")
print("Hello " + name + "!")

x = input('Enter')
print(type(x))

x = input('Enter')
r = int(x) + 4
print(r)

x = input('Enter')
r = float(x) + 5
print(r)

x = float(input('Enter number'))
y = float(input('Enter number'))
r = x + y
print('Result ' + str(r))


s = "Lets write a string as 's'"


print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")


...
