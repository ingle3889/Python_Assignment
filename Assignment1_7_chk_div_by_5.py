
def check(value):
    if (value % 5)==0:
        return True
    else:
        return False

def main():
    no1 = 0
    print("Enter the number :")
    no1 = int(input())
    ret = check(no1)
    print(ret)

if __name__ =="__main__":
    main()

