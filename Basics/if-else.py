# WAP to check if a number entered by the user is odd or even.
# Solution:

num1 = int(input("Enter your number: "))

if(num1 % 2 == 0):
    print("The entered number is even")
else:
    print("The entered number is odd")

# WAP to find the greatest of 3 numbers entered by the user
# Solution:

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
n3 = int(input("Enter your third number: "))

if((n1 > n2) and (n1 > n3)):
    print("n1 is greatest of all")
elif(n2 > n3):
    print("n2 is greatest of all")
else:
    print("n3 is greatest of all")

# WAP to find the greatest of 4 numbers entered by the user
# Solution:

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
n3 = int(input("Enter your third number: "))
n4 = int(input("Enter your forth number: "))

if((n1 > n2) and (n1 > n3) and (n1 > n4)):
    print("n1 is greatest of all")
elif((n2 > n3) and (n2 > n4)):
    print("n2 is greatest of all")
elif((n3 > n4)):
    print("n3 is greatest of all")
else:
    print("n4 is greatest of all")

# WAP to check if a number is a multiple of 7

num = int(input("Please enter your number: "))

if(num % 7 == 0):
    print("Provided number is a multiple of 7")
else:
    print("Provided number is not a multiple of 7")