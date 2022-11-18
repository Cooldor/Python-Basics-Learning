import os
CurDir = os.getcwd()

print(CurDir)

print("helpos")


cmd = "date"
os.system(cmd)

website = input()

if "https://" in website:
    os.system(website)
    print("if")

elif "www. " in website:
    website = "https://" + website
    os.system(website)

else:
    website = "https://www." + website
    os.system(website)
    print("else")


while True:
    x = int(input())

    count = 0
    y = 1

    while count < x:
        count += 1
        y *= count

    else:
        print(y)


print("103 1224 875 / 03.11.22 ")
j



