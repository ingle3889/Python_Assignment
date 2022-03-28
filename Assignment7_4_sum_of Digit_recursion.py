def Display(no):
    if no == 0:
        return 0
    digit = no % 10 
    Div = no/10   
    return (digit + Display(int(Div)))    


def main():
    no1 = int(input("Enter the number :"))
    ret = Display(no1)
    print("", ret)


if __name__ == "__main__":
    main()