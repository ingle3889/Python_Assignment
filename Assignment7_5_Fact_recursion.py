def Display(no):
    if  no == 1:
        return 1
    return no * Display(no-1)    

def main():
    no1 = int(input("Enter the number :"))
    ret = Display(no1)
    print("Factorial is :",ret)

if __name__ == "__main__":
    main()