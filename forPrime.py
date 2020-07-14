while True :
    n = int(input("Enter the number to check Prime : "))
    prime = True
    for i in range (2, n) :
        if (n % i == 0):
            prime = False
            break
    if(n == 1) :
        print("It's not a prime")
    elif prime: 
        print("It's a prime number")
    else:
        print("It's not a prime number")
        