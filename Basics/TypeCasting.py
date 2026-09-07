# Suppose if you want to add string value with any other integer value, you need to use type casting in order
# to convert the string value into integer value. Otherwise, it will give you an error.

# a = "2"
# b = 3.45

# print(a + b)  # This will give an error because you cannot add a string and a float directly.

a = int("2")
b = 3.45

print(a + b)  # This will work because we have converted the string "2" into an integer using int() function, and now we can add it to the float value 3.45.

c = 4.65
c = str(c)  # This will convert the float value 4.65 into a string value "4.65".
print(str(c))
print(type(c))