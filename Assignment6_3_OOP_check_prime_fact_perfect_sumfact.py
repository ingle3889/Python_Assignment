class Numbers:
    def __init__(self):
        self.Value = int(input("Enter the number :"))

    def ChkPrime(self):
        for x in range(2,self.Value):
            if(self.Value % x==0):
                return False
        return True

    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i
        return sum == self.Value    

    def SumFactors(self):
        Fact = 0
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                Fact = Fact + i
        return Fact    

    def Factors(self):
        print("Factor of a given number is", self.Value)
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                print(i, end=" ")
def main():
    Obj1 = Numbers()
    ret =Obj1.ChkPrime()
    print("Given number is Prime number:",ret)
    
    ret1 = Obj1.ChkPerfect()
    print("Given number is Perfect number :",ret1)
    
    ret2 = Obj1.Factors()

    ret3 =Obj1.SumFactors()
    print("")
    print("Sum of factor of given number is :",ret3)
    


if __name__ == "__main__":
    main()    
    