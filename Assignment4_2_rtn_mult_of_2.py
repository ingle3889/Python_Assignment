

# Lambda function
Mult =lambda a,b : a*b   


def main():
    no = 0
    print("Enter first number :")
    no = int(input())
    
    no1 = 0
    print("Enter second number :")
    no1 = int(input())

    ret = Mult(no , no1)
    print(ret)

if __name__ =="__main__":
    main()
