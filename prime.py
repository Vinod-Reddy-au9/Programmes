while True :
    n = int(input("Enter the number : "))
    i = 2
    if (n == 1) :
        print("It's not a prime number")
    else :
        while (i < n) :
            if(n == 2) :
                print("It's a Prime number")
                break
            elif (n % i == 0) :
                print("It's not a Prime Number")
                break
            i += 1
        else:
            print("It's a prime number")
        