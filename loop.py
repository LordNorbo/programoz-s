#while loop
i=0
while i<10:
    print(i)
    i+=1

nev=input("Mi a neved: ")
while nev=="":
    nev=input("Mi a neved: ")
print(f"Hello, {nev}!")

#ci=p * (1+ r/100) **t



osszeg=input("kérem az alap összeget: ")
while osszeg.isdigit() == False:
    print("nem jó")
    osszeg=input("kérem az alap összeget: ")
osszeg= float(osszeg)

szazalek=input("kérem a százalékot")
while szazalek.isdigit() == False:
    print("nem jó")
    szazalek=input("kérem a százalékot")
szazalek=float(szazalek)

ev=input("kérem az évek számát")
while ev.isdigit() == False:
    print("nem jó")
    ev=input("kérem az évek számát")
ev=int(ev)

ci=osszeg*(1+(szazalek/100))**ev
print(ci)


#for loop

for i in range(10):
    print(i)














