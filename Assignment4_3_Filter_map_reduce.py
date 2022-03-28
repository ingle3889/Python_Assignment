
from functools  import reduce

#def Check(a):
#    return  (a>=70 and a<=90)

Check = lambda a: a>=70 and a<=90  
#def CheckMap(no):
#    return no + 10  

CheckMap = lambda no: no+10

#def  Mult(a,b):
#    return a*b     

Mult = lambda a,b: a*b

def main():
    
    no = 0
    print("Enter the size of list")
    no = int(input())
    data = []
    for i in range(no):
        print("Enter the element")
        data.append(int(input()))
    print("Input List",data)
    CheckNum =list(filter(Check,data))  
    print("List after filter :",CheckNum) 

    Checkmap = list(map(CheckMap,CheckNum))
    print("List after Map :",Checkmap)

    Product = reduce(Mult,Checkmap)
    print("Output of reduce :",Product)



if __name__ == "__main__":
    main()    

