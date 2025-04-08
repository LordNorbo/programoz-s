class Car2:
    wheels=4
    count=0

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

        Car2.count +=1

    def drive(self):
         print(f"{self.make} {self.model} is driving.")

    