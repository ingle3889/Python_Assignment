
def Add(value1, value2):
    add =  value1 + value2
    return add
def main():
    no1 = 0
    no2 = 0
    print("Enter the first number :")
    no1 = int(input( ))
    print("Enter the second number :")
    no2 = int(input())

    ret = Add(no1, no2)
    print("addition is :",ret)
if __name__ =="__main__":
    main()

