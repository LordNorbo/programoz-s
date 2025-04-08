capitals= {
    "Hungary": "Budapest",
    "Germany": "Berlin",
    "USA": "Mexico city",
    "India": "Delhi",
    "China":"Beijing"
}
print(capitals)

print(capitals.get("Hungary"))
print(capitals.get("France"))
print(capitals.get("France","Not found"))

if capitals.get("France"):
    print("France is in the dictionary")
else:
    print("France is not in the dictionary")

if var:= capitals.get("France"):
    print("France is in the dictionary")
else:
    print("France is not in the dictionary")

if "France" in capitals:
    print("France is in the dictionary")
else:
    print("France is not in the dictionary")

if var := "France" in capitals:
    print("France is in the dictionary")
else:
    print("France is not in the dictionary")

capitals.update({"France":"Paris"})
print(capitals)

capitals.update({"USA":"Washington"})
print(capitals)

print(capitals.pop("China"))
print(capitals)

print(popped:= capitals.popitem())
print(capitals)

#capitals.clear()
#print(capitals)

keys=capitals.keys()
values=capitals.values()
items=capitals.items()

print(keys)
print(values)
print(items)

for key in keys:
    print(key)

for country, capital in capitals.items():
    print(f"{country}: {capital}")

for key, value in capitals.items():
    print(f"{key}: {value}")


menu={
    "Atom burger":5590,
    "Sajtburger":2290,
    "Bacon burger":3190,
    "Sültkrumpli":790,
    "Újratölthető üdítő":890,
    "Desszert":690
}

kaja=menu.keys()
ar=menu.values()
asd=menu.items()

for kaja, ar in menu.items():
    print(f"{kaja:>30}: {ar} Ft")

cart=[]
price=[]
buy=" "
pricelist=0
while buy!="":
    buy=input("Üdv éttermünkben! Mit szeretnél venni?")
    if buy in menu:
        
        cart.append(buy)
        price.append(menu.get(buy))
        pricelist=pricelist + menu.get(buy)
        print(f"Hozzáadta a következőt a kosárhoz: {buy}. A fizetendő ár: {pricelist} Ft")


print(f"Végösszeg: {pricelist} Ft")


















