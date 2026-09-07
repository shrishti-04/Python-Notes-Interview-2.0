# Arithemetic Operators in Python

m = 10
n = 5

print(m + n)  # Addition
print(m - n)  # Subtraction
print(m * n)  # Multiplication
print(m / n)  # Division
print(m % n)  # Modulus
print(m ** n) # Exponentiation

# Relational / Comparison Operators\

m = 10
n = 5

print(m == n)
print(m != n)
print(m > n)
print(m < n)
print(m >= n)
print(m <= n)

# Assignment Operators

num1 = 10
num1 += 5  # num1 = num1 + 5
print(num1)

num2 = 4
num2 -= 5  # num2 = num2 - 5
print(num2)

num3 = 5
num3 *= 5  # num3 = num3 * 5
print(num3)

num4 = 10
num4 /= 5  # num4 = num4 / 5
print(num4)

# Logical Operators

print(not True)
print(not False)

a = 10
b = 4

print(not(a > b))

val1 = True
val2 = True

print("AND Operator: ", val1 and val2)

val3 = True
val4 = False

print("OR Operator: ", val3 or val4)

val5 = False
val6 = False

print("OR Operator: ", val5 or val6)

print((a>b) and (a==b))
print((a>b) or (a==b))