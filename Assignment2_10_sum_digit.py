
def Sum(value):
    temp =  0
    for digit in str (value) :
        temp = temp + int(digit)
    return temp

def main():
    no1 = 0
    print("Enter the number :")
    no1 = int(input())
    getsum = Sum(no1)

    print("Sum of digits is ", getsum)
if __name__ == "__main__":
    main()