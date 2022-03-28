def factorial(value):
    if (value < 0):
        return 0
    elif (value ==0 | value == 1):
        return 1
    else:
        fact = 1
        while(value > 1):
            fact = fact * value
            value = value - 1
        return  fact

def main():
    no1 = 0
    print("Enter the number :")
    no1 = int(input())

    fact = factorial(no1)
    print("Factorial is", fact)

if __name__ == "__main__":
    main()