str1 = "Hello, World!"
str2 = "Python is awesome."

finalStr = str1 + " " + str2
print(finalStr)

# Len() 
# function provides the count of characters in a string including spaces
print(len(finalStr))

# Index 
# It provides the position of a character in a string. Index starts from 0
print(finalStr[0])  # H

# Slicing 
# It is the accessing a part of string using index.
print(finalStr[14:23])
print(finalStr[:12]) # starting from 0 to 11
print(finalStr[14:]) # starting from 14 to end of string

# Negative Slicing
# It is the accessing a part of string using negative index.

print(finalStr[-18:-1])

# Different more functions of string

str = "i am a coder"

# endwith() function checks whether the string ends with the specified value or not.
# It returns True if the string ends with the specified value, otherwise it returns False.
print(str.endswith("er"))

# capitalize() function converts the first character of the string to upper case and the rest to lower case.
print(str.capitalize())

# but if you want to capatalize in original text
str = str.capitalize()