import MarvellousNum

def ListPrime():
    no1 = 0
    no1=int(input("Enter the frequency :"))
    data= []
    for i in range(no1):
        data.append(int(input()))
    ret = MarvellousNum.ChkPrime(data)
    print(ret)


if __name__ == "__main__":
    ListPrime()