import math
class Circle():
    def __init__(self,sugar):
        self.sugar=sugar 

    def perimeter(self):
        
        kerület=2*self.sugar*math.pi
        print(kerület)
    
    def area(self):
        terület=self.sugar**2*math.pi
        print(terület)

kor1=Circle(12)
kor1.area()
kor1.perimeter()
print(kor1.sugar)


        

        







