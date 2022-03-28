
def Maximum(value):
    temp = value[0]
    for i in value:
        if i > temp:
            temp = i
    return temp
def main():
    no1 = 0
    i = 0
    print("Number of elements :")
    no1 = int(input())
    data = []
    for i in range(no1):
        data.append(int(input()))
    ret = Maximum(data)
    print(ret)

if __name__ == "__main__":
    main()