class Circle:
    PI =3.14
    def __init__(self,r): # Constructor
        self.radius = r    # Characteristics

    def Accept(self): # Behaviour
        radius =0
        radius= self.radius  
        print("Radius of a cirlce is :",radius)
    
    def Area(self): 
        Area=0
        Area = self.PI * self.radius**2
        print("Area of a cirlce is :",Area)
    
    def Circumference(self):   
        Circumference =0 
        Circumference = 2*self.PI*self.radius
        print("Circumference of a cirlce is :",Circumference)
    
    def Display(self):
        print("Radius of a circle is:",self.radius)
        self.Circumference()
        self.Area()
        
def main():
    no1= 0
    print("Enter the redius")
    no1= int(input())

    print("Value of obj1")
    obj =Circle(no1)
    obj.Accept()
    obj.Area()
    obj.Circumference
    obj.Display()
    print("")
    print("Value of obj2")
    obj1 =Circle(no1)
    obj1.Accept()
    obj1.Area()
    obj1.Circumference
    obj1.Display()
    print("")
    print("Value of obj3")
    obj3 =Circle(no1)
    obj3.Accept()
    obj3.Area()
    obj3.Circumference
    obj3.Display()

if __name__ == "__main__":
    main()    
    