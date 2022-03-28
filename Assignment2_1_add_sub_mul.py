import Arithmetic as A

def  main():
    no1 = 0
    no2 = 0

    print("Enter the first number")
    no1 = int(input())
    print("Enter the second number")
    no2 = int(input())

    #ret, ret1, ret2, ret3 = Arithmetic(no1, no2)

    ret = A.Add(no1, no2)
    print("Addition is :", ret)
    ret1 = A.Sub(no1, no2)
    print("Subtraction is :", ret1)
    ret2 = A.Mult(no1, no2)
    print("Multiplication is :", ret2)
    ret3 = A.Div(no1, no2)
    print("Division is :", ret3)

if __name__ == "__main__":
    main()