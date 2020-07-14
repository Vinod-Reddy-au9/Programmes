while True :
    c = int(input("Enter the number : "))
    n = c+1
    for i in range (1, n) :
        print(" " * (i-1), end="")
        print("*" * (n-i))
    print()
    