food=str
price=int
stock=int


foods= ["alma","körte","sajt","szilva"]
prices= [1000,2000,3000,4000]
stocks= [5,10,15,20]

for food, price, stock in zip(foods,prices,stocks):
    print(f"{food:^}: {stock:^2}: {price:^10.2f} HUF")


numbers= [11,19,7,-3,0]
print(numbers)
doubled= [x * 2 for x in numbers]
print(doubled)
filtered= [x*2 for x in numbers if x>0]
print(filtered)

numbers= [5,8,3,11,12]
even=[x for x in numbers[::2] if x% 2==0]
print(even)

word=str

words= ["lámpa","almafa","essa"]
for word in words:
    print(word)

for char in "almafa":
    print(char)

for i,word in enumerate("almafa"):
    print(f"{i}. {word}")

for i,word in enumerate("almafa",1):
    print(f"{i}. {word}")

for _ in range(1,5,2):
    print("alma")

#walrus operator :=

my_list= [1,2,3,4]
if(n:=len(my_list)) >5:
    print(f"List has {n} elements")
else:
    print("List has less than 5 elements")


while(line:=input("bekérés:"))=="":
    print(line)

while(num:=int(input("adj meg egy pozitív számot! ")))>0:
    print(num)

#list comprehersion
numbers= [x for x in range(10) if (y:=x*2) >5]
print(numbers)

numbers= [x * 2 for x in range(10) if (y:=x*2) >5]
print(numbers)

#Multiple assignments
x,y,z=1,2,3
print(x)
print(y)
print(z)

#Unpacking with *
numbers=[1,2,3,4,5]
x,*y,z =numbers
print(x)
print(y)
print(z)

#Unpacking with _
numbers=[1,2,3,4,5]
x,_,y,_,z=numbers
print(x)
print(y)
print(z)

keypad=(
    ("1","2","3"),
    ("4","5","6"),
    ("7","8","9"),
    ("*","0","#")
)

print(keypad)







