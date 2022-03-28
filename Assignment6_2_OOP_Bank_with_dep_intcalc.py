class Bank_Account:
    ROI = 10.5
    def __init__(self): 
        self.Name = str(input("Enter your name :"))
        self.Amount=0
        print("Hi",self.Name," your available balance is :",self.Amount)
 
    def Deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.Amount =  self.Amount + amount
        print("Hi",self.Name," you have deposited amount is :",amount)
 
    def Withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.Amount >= amount:
            self.Amount = self.Amount -amount
            print("Hi",self.Name, "You have withdrew:", amount)
        else:
            print("Hi", self.Name ,"Insufficient balance in account ")
 
    def Display(self):
        print("Hi", self.Name, "Available Balance=", self.Amount)
        #print("Net Available Balance=", self.balance)

    def CalculateIntrest(self):
        amount = (self.Amount /100) * Bank_Account.ROI
        print("Hi", self.Name, "Interest accumalated amount =",amount)
    

def main():
    obj = Bank_Account()
    obj.Deposit()
    obj.Withdraw()
    obj.Display()
    obj.CalculateIntrest()
    print("")
    obj1 = Bank_Account()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.Display()
    obj1.CalculateIntrest()
    print("")
    obj2 = Bank_Account()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.Display()
    obj2.CalculateIntrest()

    


if __name__ == "__main__":
    main()    
    