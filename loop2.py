#for loop

for i in range(10):
    print(i)

for i in range(5,10):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(0,10,-1):
    print(i)

for i in reversed(range(10)):
    print(i)

hello="Hello World!"
for i in range(len(hello)):
    print(i)

for i in hello:
    print(i)

for i in range(len(hello)):
    print(hello[i])

#continue, break, pass

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        pass
    print(i)

import time

for i in reversed(range(11)):
    print(i)
    time.sleep(1)

mettol=input("Mettől?")
meddig=input("Meddig?")
mp=input("Hány másodpercig?")
irany=input("Melyik irányba?")

for i in range(mettol,meddig):
    print(i)
    time.sleep(mp)



