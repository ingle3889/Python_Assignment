def ChkPrime(value):
    sum=0
    for i in range(len(value)):
        temp = value[i]
        for num in range(2, temp+1):
            # all prime numbers are greater than 1
            if temp > 1:
                for i in range(2, temp):
                    if (temp % i) == 0:
                        break
                else:
                    sum = sum   + temp
                    break
    return sum