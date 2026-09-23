# WAP to ask the user to enter names of their three favourite movies and store in in list.

from numpy import append


a = input("Enter your first movie name: ")
b = input("Enter your second movie name: ")
c = input("Enter your third movie name: ")

lists = []

lists.append(a)
lists.append(b)
lists.append(c)

print("Here are the lists of your favourite movies:", ' ,'.join(lists))

# WAP to check if a list contains a pallindrome of elements.

from itertools import count


p = input("Enter your first element: ")
q = input("Enter your second element: ")
r = input("Enter your third element: ")
s = input("Enter your forth element: ")
t = input("Enter your fifth element: ")

list1 = []

list1.append(p)
list1.append(q)
list1.append(r)
list1.append(s)
list1.append(t)

if(list1 == list1[::-1]):
    print("Provided list contains pallindrome elements")
else:
    print("Provided list does not contains pallindrome elements")

# WAP to count the number of students with the "A" grade in the following tuple.

tuples = ('C', 'D', 'A', 'A', 'B', 'B', 'A')

print(f"The are {tuples.count("A")} students who have scored A grade")

# Store the above value in list and sort them from A to D

list2 = list(tuples)
list2.sort()
print(list2)

