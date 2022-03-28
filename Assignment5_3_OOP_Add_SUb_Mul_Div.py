class Arithmetic:
    def __init__(self,a,b): # Constructor
        self.no1 = a 
        self.no2 = b    # Characteristics

    def Accept(self): # Behaviour
        Value1 =0
        Value2 =0
        Value1 = self.no1
        Value2 = self.no2 
        sum =self.Addition(Value1,Value2)
        sub =self.Subtraction(Value1,Value2)
        Multi =self.Multiplication(Value1,Value2)
        Div =self.Division(Value1,Value2)
        print("Addition is :",sum)
        print("Substraction is :",sub)
        print("Multiplication is :",Multi)
        print("Division is :",Div)
        

    def Addition(self,Value1,Value2):
        sum =0
        sum = Value1 + Value2
        return sum

    def Subtraction(self,Value1,Value2):
        sub =0
        sub = Value1 - Value2
        return sub    

    def Multiplication(self,Value1,Value2):
        Mul = 0
        Mul = Value1 * Value2
        return Mul     
    
    def Division(self,Value1,Value2):
        Div = 0
        Div = Value1 / Value2
        return Div 
        
def main():
    no1= 0
    print("Enter the first number")
    no1= int(input())
    no2= 0
    print("Enter the second number")
    no2= int(input())
    
    print()
    print("Printing value of obj")
    obj =Arithmetic(no1, no2)
    obj.Accept()
    
    print()
    print("Printing value of obj1")
    obj1 =Arithmetic(no1, no2)
    obj1.Accept()
    
    print()
    print("Printing value of obj2")
    obj2 =Arithmetic(no1, no2)
    obj2.Accept()
    


if __name__ == "__main__":
    main()    
    