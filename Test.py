import os
import time

# os.system("open https://www.youtube.com/")

time.sleep(5)


for i in os.walk("/Users/air/Desktop/все/ONIX/Каталог ONIX 2018 новый (весна)"):
    print(i)
    break


lists = []

for address, dirs, files in os.walk("/Users/air/Desktop/все/ONIX/Каталог ONIX 2018 новый (весна)"):
    for file in files:
        lists.append(os.path.join(address, file))      # shows all file paths in the indicated direction
print(lists)


lists_path = []

for address, dirs, files in os.walk("/Users/air/Desktop/все/ONIX/Каталог ONIX 2018 новый (весна)"):
    for file in files:
        full = os.path.join(address, file)
        if ".jpg" in full:                      # shows files but only with .jpg
            lists_path.append(full)
print(lists_path)


lists = []

for address, dirs, files in os.walk("/Users/air/Desktop/все/ONIX/Каталог ONIX 2018 новый (весна)"):
    for file in files:
        full = os.path.join(address, file)
        if time.time() - os.path.getctime(full) < 86400:            # show files that were created 24 hours ago
            lists.append(full)
print(lists)

# "r" open for reading (by default)
# "t" open in text format (by default)
# "w" open for writing, the contents of the file are deleted, if no such file, it will create the new one
# "a" open for append a file in the end, if no such file, it will create the new one
# "b" open in binary mode
# "+" open for reading and writing "r+", "w+", "a+"

r = open("/Users/air/Desktop/text.txt", "w")
r.write("Hello user")                   # created a txt file + wrote there "hello user"
r.close()


r = open("/Users/air/Desktop/text.txt")
u = r.read()                              # read the file and saved information from there in a variable
print(u)
r.close()

r = open("/Users/air/Desktop/text.txt", "w")
for x in lists_path:
    r.write(x + "\n")                       # wrote all file paths in txt file

r.close()


r = open("/Users/air/Desktop/text.txt")
for i in r:
    if "ONIX" in i:                         # shows all file paths for specific qualifying string
        print(i)
r.close()

# for binary files working

# r = open("e.exe", "rb")        # read(r) "b" means read in binary mode
# y = open("copy e.exe", "wb")   # create(w) the file in binary mode "b",because we can not work with binary code itself

# while True:
    # var = r.read(1048576)   1 MB form bytes
    # print(var.__sizeof__())
    # if var.__sizeof__() == 17:
        # break
    # y.write(var)

# print(control)
# r.close()
# y.close()












