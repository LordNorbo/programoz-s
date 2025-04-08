from  abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius)-> None:
        self.radius= radius
    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side)-> None:
        self.side=side
    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self,base,height)->None:
        self.base=base
        self.height=height
    def area(self):
        return 0.5* self.base * self.height

shapes=[Circle(5),Square(4),Triangle(3,6)]

class Pizza(Circle):
    def __init__(self, radius,topping)->None:
        super().__init__(radius)
        self.topping=topping

for shape in shapes:
    print(shape.area())


shapes=[Circle(5),Square(4),Triangle(3,6),Pizza(3,"pepperoni")]





def hello():
    print("Hello!")

obj= hello
obj()

def hello(fn):
    def inner():
        print("Hello", end = " ")
        fn()
    return inner

def world():
    print("World! 1")

decorated=hello(world)
decorated()

@hello
def world():
    print("World! 2")

world()

@hello
def world():
    print("World! 3")

world()

import time

def measure_time(fn):
    def inner(*args,**kwargs):
        start=time.time()
        result=fn(*args,**kwargs)
        end=time.time()
        print(end - start)
        return result
    return inner

@measure_time
def hello():
    time.sleep(1)
    print("Hello, World!", end= " ")

hello()

@measure_time
def world():
    time.sleep(2)
    print("World!", end= " ")
world()

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")


class Car:
    def horn(self):
        print("Beep!")
    def speak(self):
        self.horn()


animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(Animal.alive)


