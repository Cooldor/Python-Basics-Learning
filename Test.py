import os
import time

for i in os.walk("/Users/air/Desktop/все/ONIX/Каталог ONIX 2018 новый (весна)"):
    print(i)
    break


lists = []

for adress, dirs, files in os.walk("/Users/air/Desktop/все/ONIX/Каталог ONIX 2018 новый (весна)"):
    for file in files:
        lists.append(os.path.join(adress, file))
print(lists)






lislts = []

for adress, dirs, files in os.walk("/Users/air/Desktop/все/ONIX/Каталог ONIX 2018 новый (весна)"):
    for file in files:
        full = os.path.join(adress, file)
        if ".jpg" in full:
            lists.append(full)
print(lists)






lislts = []

for adress, dirs, files in os.walk("/Users/air/Desktop/все/ONIX/Каталог ONIX 2018 новый (весна)"):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:
            lists.append(full)
print(lists)
























