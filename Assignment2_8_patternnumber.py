
def main():
    no1 = 0
    print("Enter the frequency :")
    no1 = int(input())

    for i in range(no1):
        j=1
        for j in range(i+1):
            print(j+1, end=" ")
            j = j + 1
        print(" ")


if __name__ == "__main__":
    main()