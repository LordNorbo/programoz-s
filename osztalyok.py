class Car:
    wheels=4
    count=0
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

        Car.count += 1

    def drive(self):
        print(f"{self.make} {self.model} is driving.")

my_car=Car("Toyota","Camry",2022)
print(my_car)
print(my_car.make)
my_car.drive()

my_car2=Car("Fiat","Multipla",2012)
print(my_car2)
print(my_car2.make)
print(my_car2.year)

my_car2.drive()

from auto import Car2

my_car3=Car2("Volkswagen","Passat", 2006)
print(my_car3)
print(my_car3.make)

my_car3.drive()

print(Car.wheels)
print(Car.count)

class ElectricCar(Car):
    def __init__(self, make, model, year,battery_size):
        super().__init__(make,model,year)
        self.battery_size=battery_size
    
    def drive(self):
        print(f"{self.make} {self.model} is driving with an electric battery.")
my_electric_car= ElectricCar("Tesla","Model S",2022,100)
my_electric_car.drive()

print(my_electric_car.battery_size)
print(my_electric_car.wheels)

print(issubclass(ElectricCar,Car))
print(isinstance(my_electric_car,ElectricCar))
print(isinstance(my_electric_car,Car))


class Animal:
    def __init__(self,name,age,domesticated):
        self.name=name
        self.age=age
        self.domesticated=domesticated
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
class Dog(Animal):
    def __init__(self, name, age, domesticated,breed,sex):
        super().__init__(name, age, domesticated)
        self.breed=breed
        self.sex=sex

    def bark(self):
        print(f"{self.name} is barking.")

    def play(self):
        print(f"{self.name} is playing.")

my_animal=Animal("oroszlán",12,False)
print(my_animal.name)
my_animal.eat()

my_animal2= Dog("kutya",10,True,"Golden Retriever","Male")    







