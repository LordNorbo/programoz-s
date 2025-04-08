#1. változók és típuskonverzió
# 1. feladat:
# Írj egy függvényt, amely két bemenetet vesz fel: egy stringet és egy egész zsámot
#A függvénynek össze kell fűznie a stringet az egész számmal(miután az egész számot striggé konvertálta), és vissza kell adnia az eredményt.

def osszefuzo(s,n):
    return s + str(n)

eredmény=osszefuzo("Kor: ", 25)
print(eredmény)

#2. feladat:
#Írj eg függvényt, amely beolvassa a felhasználó nevét és életkorát, majd kiír egy üdvözlő üzenetet, amely tartalmazza anevet és az életkort

def udvozlo(nev,eletkor):
    print(f"Üdvözöllek {nev}, az életkorod: {eletkor}")

udvozlo("Norbo",20)

#3. feladat
#Írj egy függvényt, amely egy számot vesz fel bemenetként, és visszaadja, hogy a szám pozitív, negatív vagy nulla

def szam(num):
    if num<0:
        return "A szám negatív"
    if num>0:
        return "A szám pozitív"
    else:
        return "A szám nulla"

es=szam(20)
print(es)

#4. feladat
#Írj egy függvényt, amely kiírja az összes páros számot 1-től egy adott számig egy for ciklus segírségével

def paros(ig):
    for i in range(1,ig):
        if(i%2==0):
            print(i)

paros(21)

#5. feladat
# Írj egy függvényt, amely egy számokból álló listát vesz fel, és visszadja a lista összes számának összegét

def lista(num):
    return sum(num)
 
print(lista(num=[1,2,45,78]))

#6. feladat
#Írj egy függvényt ,amely generál egy véletlenszámot 1 és 100 között, és megkéri a felhasználót, hogy találja ki a számot. A függvénynek visszajelzést kell adnia, ha a tipp túl magas, alacsony vagy helyes

import random

#def veletlen(tipp):
#    ran = random.randint(1,100)
#    while tipp!=ran:
#        tipp=int(input("Adj meg egy tippet: "))
#        if tipp>ran:
#            print("Alacsonyabbat tippelj!")
#        if tipp<ran:
#            print("Magasabbat tippelj!")
#        if tipp==ran:
#           print(f"Gratulálok, eltaláltad a számot!")

#veletlen(1)

#7. feladat
#Írj egy függvényt, amely egy vegyes típusú elemeket tartalmazó listát vesz fel( egész számok és stringek), és visszaad egy új listát, amelyben minden elem stringgé van konvertálva.

#def konvertalo(halmaz):
#   return[str(elem) for elem in halmaz]
#       
#eredmeny=konvertalo([1,"asd",3.7,True])
#print(eredmeny)

#8. feladat
#Írj egy függvényt, amely megkérdezi a felhasználót a kedvenc színéről, majd kiír egy üzenetet, hogy "A kedvenc színed a [szín]"

#def szin(szined):
#    szined=input("Mi a kedvenc színed?")
#    print(f"A kedvenc színed a {szined}")

#szin()

#9. feladat
#Írj egy függvényt, amely egyy évet vesz fel bemenetként, és visszaadja, hogy az év szökőév-e vagy sem.

def szoko(ev):
    if ev%4==0:
        print("Az év szökőév")
    else:
        print("Nem szökőév")    

szoko(2000)
szoko(2002)

#10. feladat
#Írj egy függvényt, amely egy számot vesz fel bemenetként, és kiírja a szorzótáblát 1-10-ig

def szorzotabla(numero):
    for i in range(11):
        print(numero*i)

szorzotabla(2)

#11. feladat
#Írj egy programot, amely tartalmaz egy "osszegzo" nevű függvényt, ami a paramétereként átvett listaelemeket(egész számokat) összeadja és az összegükkel tér vissza

def osszegzo(listaaa):
    return sum(listaaa)

print(osszegzo(listaaa=[22,2,67]))

def osszegzoo(szamokk):
    osszeg=0
    for szam in szamokk:
        osszeg+=szam
        return osszeg

print(osszegzoo(szamokk=[1,2,5,7]))

#12. feladat
#Írj egy programot, amely tartalmaz egy "paros_e" nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek(egész számok) között van páros,
# ellenkező esetben a vissztérési érték False
ertek=False
def paros_e(esa):
    for essa in esa:
        if essa%2==0:
            ertek=True
        else:
            ertek=False
    return ertek

print(paros_e(esa=[1,3,5,7,8]))

#13. feladat
# #Írj egy programot amely tartalmaz egy "harommal_oszthatok" nevu függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van

def harommal_oszthatok(dropa):
    harmas=0
    for dropi in dropa:
        if dropi % 3 == 0:
            harmas=harmas+1
    return harmas

print(harommal_oszthatok(dropa=[1,2,3,4,5,6,]))

#13.2 feladat
# A felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje a függvény(ADDIG TARTSON AMÍG NEGATÍV SZÁMOT NEM AD A FELHASZNÁLÓ)

def harommal_oszthatok2():
    asd=[]
    while True:
        bekert=int(input("Kérek egész számokat: "))
        asd.append(bekert)
        if bekert<0:
            break
    return harommal_oszthatok(asd)
    

print(harommal_oszthatok2())

#14. feladat
# Írj egy programot, amelyben van egy "kerulet" nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is.
# Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét(0 tetszőleges paraméter:négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszög, 3 vagy több tetszőleges paraméter:sokszög)

def kerulet(a, b=None, c=None, d=None, e=None):
    if b is None:
        return 4 * a
    elif c is None:
        return 2 * (a + b)
    elif d is None:
        return a + b + c
    elif e is None:
        return a + b + c + d
    else:
        return a + b + c + d + e

print(kerulet(4))             
print(kerulet(4, 5))          
print(kerulet(3, 4, 5))       
print(kerulet(1, 2, 3, 4))    
print(kerulet(1, 2, 3, 4, 5)) 


#15. feladat
#Írj egy programot, ami addig kér be pozitív számokat, amíg a felhasználó negatív számot nem ír. A megadott számokat tárolja a program egy listában, és azt adja át paraméterként egy függvénynek
# amely a lista legkisebb elemével tér vissza. A program írja ki, hogy melyik volt a megadott legkisebb szám

def pozi():
    nyinya=[]
    while True:
        bekeres=int(input("Kérek egész számokat: "))
        if bekeres>0:
            nyinya.append(bekeres)
        if bekeres<0:
            break
    return min(nyinya)

print(pozi())
































