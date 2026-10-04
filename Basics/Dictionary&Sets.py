# Store the following word meanings in a python dictionary:
# 
# table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"

from itertools import count


dict1 = {"table": ["a piece of furniture", "list of facts & figures"],
         "cat": "a small animal"}

print(dict1)

# You are given a list of subjects for students. Assume one
# classroom is required for 1 subject. How many classrooms are needed by all students.

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

print(f"Total {len(subjects)} classrooms are needed per subjects for students.")

# WAP to enter marks of 3 subjects from the user and store them in a dictionalry. Start
#  with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

chem = int(input("Enter your Chemistry marks: "))
marks.update({"Chemistry": chem})

phy = int(input("Enter your Physics marks: "))
marks.update({"Physics": phy})

maths = int(input("Enter your Maths marks: "))
marks.update({"Maths": maths})

print(marks)

# Figure out a way to store 9 & 9.0 as separate values in the set

values = {
    {"integer": 9},
    {"float": 9.0}
}