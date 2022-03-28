
def Prime(value):

    if(value >1):
        for i in range(2, value):
            if (value % i) !=0:
                print("It is Prime Number")
                break
            else:
                print("It is not a Prime Number")
                break

def main():
    no1 = 0
    print("Enter the number :")
    no1 = int(input())
    Prime(no1)


if __name__ == "__main__":
    main()