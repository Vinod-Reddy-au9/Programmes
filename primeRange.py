def isPrime(n):
    for i in range (2, n+1):
        if(n % i == 0 and n != i):
            return False
    return True


if __name__ == "__main__":
    while True :    
        n = int(input("Enter the number : "))
        primes = []
        for i in range (2, n+1):
            if isPrime(i):
                primes.append(i)
        print(primes)

