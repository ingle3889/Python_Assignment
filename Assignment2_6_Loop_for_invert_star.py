
def main():
    no1 = 0
    print("Enter the frequency :")
    no1 = int(input())

    for i in range(0,no1):
        print("* "*no1)
        no1 = no1 - 1


if __name__ == "__main__":
    main()