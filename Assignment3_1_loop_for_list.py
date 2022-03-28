
def Addition(value):
    temp = 0

    for i in range(len(value)):
        temp = temp + value[i]
    return  temp


def main():
    no1 = 0
    i = 0

    print("Number of elements :")
    no1 = int(input())
    data = []
    for i in range (no1):
        data.append(int(input()))
    ret = Addition(data)
    print(ret)
if __name__ == "__main__":
    main()