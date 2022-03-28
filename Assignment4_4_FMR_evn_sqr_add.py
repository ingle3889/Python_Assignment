
from functools  import reduce

def Even(a):
    return a%2 ==0 

#Even = lambda a: (a%2 == 0)

def Product(a):
    return a**2

#Product = lambda a: a**2

def Red(a,b):
    return a+b
#Red = lambda a,b: a+b

def main():
    no = 0
    print("Enter the size of :")
    no = int(input())
    data = []
    for i in range(no): 
        data.append(int(input()))
    print("Input list ",data)

    Checkeven = list(filter(Even, data))
    print("list after filter ",Checkeven) 

    Prod = list(map(Product, Checkeven))
    print("list after map ",Prod) 

    Rad = reduce(Red, Prod)    
    print("list after reduce ",Rad) 



if __name__ == "__main__":
    main()