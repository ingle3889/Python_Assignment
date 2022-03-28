def Display(no, count = 1):
    if no > 0: 
        print(count) 
        no = no - 1
        count = count + 1
        Display(no, count)
        


def main():
    no1 = int(input("Enter the number :"))
    Display(no1)



if __name__ == "__main__":
    main()