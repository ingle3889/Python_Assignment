
def factor(value):
    factor = 0
    for i in range(1, value - 1):
        if value % i == 0:
            factor = factor + i
    return factor

def main():
    no1 = 0
    print("Enter the number :")
    no1 = int(input())
    getsum = factor(no1)

    print("Sum of digits is ", getsum)
if __name__ == "__main__":
    main()