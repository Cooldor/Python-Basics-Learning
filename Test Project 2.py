import os

CurDir = os.getcwd()
print(CurDir)

# help.os for info


cmd = "date"
os.system(cmd)


while True:
    website = input("Enter your website:\n")
    if website == "end":
        break

    if "https://" in website:
        os.system("open " + website)
        print("if")

    elif "www. " in website:
        website = "https://" + website
        os.system("open " + website)
        print("elif")

    else:
        website = "https://www." + website
        os.system("open " + website)
        print("else")


# Another Factorial cycle (loop)
while True:
    x = int(input("Enter your number:\n"))
    if x == -1:
        break
    count = 0
    y = 1

    while count < x:
        count += 1
        y *= count

    else:
        print(y)


print("103 1224 875 / 03.11.22 , 240 11 4 / 05.12.22")
print("end of program")



