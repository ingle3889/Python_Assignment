
from functools  import reduce

def Prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            return num

def Add2(a):
    return a*2

def Redcap(a,b):
    if a > b:
        return a
    else:
        return b           
def main():
    no = 0
    print("Enter the size of list :")
    no = int(input())
    data= []
    for i in range(no):
        data.append(int(input()))
    
    print("Input list :",data)

    prime = list(filter(Prime,data))
    print("List after filter :",prime)

    add2 = list(map(Add2,prime))
    print("List after map :",add2)

    redcap = reduce(Redcap,add2)
    print("Output of reduce :",redcap)

if __name__ == "__main__":
    main()    