a = int(input("Enter your English marks : "))
b = int(input("Enter your Maths marks : "))
c = int(input("Enter your Physics marks : "))
d = int(input("Enter your Social marks : "))
e = int(input("Enter your CC marks : "))

avg = (a+b+c+d+e)/5

print(avg)

if (avg >= 90):
    print("Your grade is : A")
elif (avg >=70 and avg <90):
    print("Your grade is : B")
elif (avg >= 50 and avg < 70):
    print("Your grade is : C")
elif (avg >= 30 and avg < 50):
    print("Your grade is : D")
else:
    print("Your grade is : E")