def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f(a,L=None)->list:
    if L is None:
        L=[]
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


def parrot(voltage,state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "vikts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action="VOOOOOOOM")
parrot(action="VOOOOOOOOM", voltage=1000000)
parrot("a million","bereft of life","jump")
parrot("a thousand", state="pushing up the daises")


import math

megoldas=0

def összeadás(a,b):
    megoldas= a+b
    print(megoldas)
    return a,b,megoldas

def kivonás(a,b):
    megoldas= a-b
    print(megoldas)
    return a,b,megoldas

def szorzás(a,b):
    megoldas= a*b
    print(megoldas)
    return a,b,megoldas

def osztás(a,b):
    megoldas= a/b
    print(megoldas)
    return a,b,megoldas

exit=False

while not exit:
    a=(input("Kérem az első számot: "))
    if(not a.isdigit()):
         print("Számot írj!")
         continue
    a=int(a)
    művelet=input("Kérem a műveletet: ")
    
    b=(input("Kérem a második számot: "))
    if(not b.isdigit()):
         print("Számot írj!")
         continue
    b=int(b)

    if művelet=="+":
        összeadás(a,b)
    if művelet=="-":
        kivonás(a,b)
    if művelet=="*":
        szorzás(a,b)
    if művelet=="/":
        osztás(a,b)
    quit= input("Akarsz még számolni? i/n: ")
    if quit.lower()=="n":
        exit=True
    if quit.lower()=="i":
        continue


my_list=1
try:
    iter(my_list)
    print("My list is iterable")
except TypeError:
    print("My list is not iterable")

my_list=[1,2,3]
try:
    iter(my_list)
    print(my_list)
except TypeError:
    print("Type Error")

#dictionary={"a":1,"b":2,"c":3}
#print(type(dictionary))
#for key, value in dictionary.items():
#    print(key, value)

file= open("file.txt","r")
print(type(file))
for line in file:
    print(line)



word="word"
letter=input("Tippelj egy betűt: ")

if letter in word:
    print("Ügyes vagy,"+ letter +" betű benne van a szóban!")
else:
    print("Sajnos a/az "+ letter +" nincs benne a szóban!")

szó="dropa"

élet=15
bruh=True

while bruh==True:
    tipp=input("Kérek egy szót: ")
    if tipp in szó:
        print(f"Gratulálok, {tipp} benne van a szóban! Ennyi életed maradt:{élet}")
    
    else:
        élet=élet-1
        print(f"Sajnos {tipp} betű nincs a szóban! Ennyi életed maradt:{élet}")
    
    if tipp in szó:
        for char in szó:
            if char in szó:
                print(char,end="")
            else:
                print("_",end="")
    
    if élet==0:
        bruh=False
        print(f"Sajnos elfogyott az összes életed, a szó amit ki kellett volna találnod:{szó}")
    
    if vonal==szó:
        bruh=False
        print(f"Gratulálok, kitaláltad a szót, {szó}. Ennyi életed maradt: {élet}")

import random















