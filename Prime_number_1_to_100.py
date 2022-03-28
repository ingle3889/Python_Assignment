

def main():
    no=0
    print("Enter the range :")
    no = int(input())
    data=[]
    for num in range(2,no):
        count =0
        for i in range(2,num):
            if (num % i)== 0: 
                count = count +1
                break
        if (count == 0 and num!=1):
            data.append(num)        

    print(data)                           
if __name__ == "__main__":
    main()    