
def Minimum(value):
    temp = value[0]

    for i in value:
        if i < temp:
            temp = i
    return temp
def main():
    no1= 0
    no1 = int(input("Number of elements :"))
    data = []
    for i in range(no1):
        data.append(int(input()))

    ret = Minimum(data)
    print(ret)

if __name__ =="__main__":
    main()