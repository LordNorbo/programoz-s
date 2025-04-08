""""
class Prey:
    def flee(self):
        print("The prey is fleeing")

class Predator:
    def hunt(self):
        print("The predator is hunting")
"""

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Rabbit(Prey):
    pass

class Lion(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit=Rabbit("Rabbit", 3)
lion=Lion("Lion", 5)
fish=Fish("Fish",1)

fish.flee()
fish.hunt()
lion.hunt()
rabbit.flee()

lion.eat()
rabbit.eat()


x="Hello World!"
print(len(x))

mylist=["apple","banana","cherry"]
print(len(mylist))
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year" :1966
    }

print(len(thisdict))

class Vehicle:
    def move(self):
        print("Move!")
class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

class Car(Vehicle):
    def move(self):
        print("Drive!")

boat=Boat()
plane=Plane()
car=Car()

for vehicle in (boat,plane,car):
    vehicle.move()


class Super:
    def __init__(self):
        self.name="Super"

class Sub(Super):
    def __init__(self):
        super().__init__()

sup=Super()
print(sup.name)
sub=Sub()
print(sub.name)

class Shape:
    def __init__(self,color,border):
        self.name="Shape"
        self.color=color
        self.border=border

    def info(self):
        print(f"{self.name}, Color: {self.color}, Border: {self.border}")
    
class Circle(Shape):
    def __init__(self, color, border,radius):
        super().__init__(color, border)
        self.radius=radius

class Square(Shape):
    def __init__(self, color, border,a):
        super().__init__(color, border)
        self.a=a

class Rectangle(Square):
    def __init__(self, color, border, a,b):
        super().__init__(color, border, a)
        self.b=b
        self.a=a

circle=Circle("Blue","Thick",5)
square=Square("Yellow","Thin",6)
rectangle=Rectangle("Red","Thin",8,4)

print(circle.color)
print(circle.border)
print(circle.radius)

print(square.color,square.border,square.a)
print(f"Rectangle első oldala: {rectangle.a}, rectangle második oldala: {rectangle.b}")

Shape.info(circle)
Shape.info(square)
Shape.info(rectangle)

class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")
        #super().method()

a=A()
b=B()
a.method()
b.method()







