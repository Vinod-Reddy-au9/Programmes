choice = int(input("\nfor Addition          1 \nfor Subtraction       2 \nfor Multiplication    3 \nfor Division enter    4\n\nEnter the number Your choice : "))

a = int(input("\nEnter number 1 : "))
b = int(input("Enter number 2 : "))

add = a+b
sub = a-b
mul = a*b
div = a/b


if (choice == 1):
    print(add)
elif (choice == 2):
    print(sub)
elif (choice == 3):
    print(mul)
elif(choice == 4):
    print(div)    
else:
    print("\nBrain doesn't work, Enter the number you see...!")
    print("Just kidding, Choose the number which was listed...! ")