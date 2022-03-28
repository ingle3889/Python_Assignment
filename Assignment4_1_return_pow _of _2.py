#named function


# Lambda function
Pow =lambda a : a**2   


def main():
    no = 0
    print("Enter the number :")
    no = int(input())

    ret = Pow(no)
    print(ret)

if __name__ =="__main__":
    main()
