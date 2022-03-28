
def Chknum(value):
    count = 0
    temp= value[0]
    num=0
    num=str(input("Element to search :"))
    for i in range(len(value)):
        temp = value[i]
        if temp == num:
            count = count + 1
    return count
def main():
    no1 = 0
    no1= int(input("Number of elements :"))
    data = []
    for i in range(no1):
        data.append(input())
    ret = Chknum(data)
    print( ret)

if __name__ == "__main__":
    main()