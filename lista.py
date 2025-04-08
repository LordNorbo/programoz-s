#collections
#list, tuple, set, dict
#list= []
#tuple= ()
#set= {}
fruit="apple"
fruits=["apple","banana","cherry"]

print(fruits[0])
print(fruits[:1])
print(fruits[::2])

for fruit in fruits:
    print(fruit)

print("apple" in fruits)
print("orange" in fruits)

fruits.append("orange")
print("orange" in fruits)
print(fruits)

fruits.insert(1,"mango")
print(fruits)

fruits.remove("cherry")
print(fruits)

fruits.pop()
print(fruits)

fruits[0]="pineapple"
print(fruits)

print(len(fruits))

print(fruits.count("apple"))
print(fruits.count("pineapple"))
print(fruits.index("pineapple"))

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)


#set

fruits={"apple","banana","cherry"}
print(fruits)

print("banana" in fruits)

fruits.add("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

#tuple

fruits=("apple","banana","cherry")
print(fruits)

print(fruits[0])

print(fruits.count("apple"))

print(fruits.index("apple"))

import math

lista=[]
arlista=[]
teljesar=0

kocsi=input("Mit veszel? ")
lista.append(kocsi)
ar=int(input("Mennyiért vetted?"))
arlista.append(ar)
teljesar=teljesar+ar
while kocsi != ""  and ar!="0":
    kocsi=input("Mit veszel? ")
    lista.append(kocsi)
    ar=int(input("Mennyiért vetted?"))
    arlista.append(ar)
    teljesar=teljesar+ar
lista.remove("")
arlista.remove(0)
print(lista)
print(arlista)
print(teljesar)
for kocsi in lista:
    print(f"{kocsi}: {arlista[lista.index(kocsi)]}Ft")
print(f"Teljes összeg: {teljesar}Ft")











