while True :
    n = int(input("Enter number : "))
    for i in range (1, n) :
        print(" " * (n-i), end="")
        print("* " * (i))
    print()