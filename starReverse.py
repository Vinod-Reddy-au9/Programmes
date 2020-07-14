c = int(input("Enter number : "))
n = c+1
row = 1
while (row <= n) :
    print(" " * (row-1), end = "")
    print("*" * (n-row) )
    row += 1