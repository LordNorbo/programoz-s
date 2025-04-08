
kerdesek=["1. kérdés: 2 + ? = 20","2. kérdés: Melyik évben koronázták királlyá Hunyadi Mátyást?","3. kérdés: Melyik magyar költő volt forradalmár?"]
valaszlehetosegek=["18, 16, 19","1458 , 1469 , 1452 ","Radnóti Miklós, Ady Endre, Petőfi Sándor"]
jovalaszok=["18","1458","Petőfi Sándor"]
pontok=0

print(kerdesek[0])
print(valaszlehetosegek[0])
valasz1=input("Az első válasz: ")
if valasz1==jovalaszok[0]:
    pontok=pontok+1
    print("Jó válasz!")
if valasz1!=jovalaszok[0]:
    print("Rossz válasz!")

print(kerdesek[1])
print(valaszlehetosegek[1])
valasz2=input("A második válasz: ")
if valasz2==jovalaszok[1]:
    pontok=pontok+1
    print("Jó válasz!")
if valasz1!=jovalaszok[1]:
    print("Rossz válasz!")

print(kerdesek[2])
print(valaszlehetosegek[2])
valasz2=input("A második válasz: ")
if valasz2==jovalaszok[2]:
    pontok=pontok+1
    print("Jó válasz!")
if valasz1!=jovalaszok[2]:
    print("Rossz válasz!")
print(pontok)
























