# # Print the sum of odd and even numbers

# from itertools import count


# lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd = 0
# even = 0

# for i in range(len(lists)):
#     if(i % 2 == 0):
#         even += lists[i]
#     else:
#         odd += lists[i]

# print(odd, even)

# # Sum of pairs using single arrays

# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = len(lis)

# for i in range(n):
#     for j in range(i+1, n):
#         sum = lis[i] + lis[j]
#         print(sum, end=' ')

# # Sum of pairs using two arrays

# arr1 = [1, 2, 3, 4]
# arr2 = [5, 6, 7, 8]

# n = len(arr1)
# m = len(arr2)

# for i in range(n):
#     for j in range(m):
#         sums = arr1[i] + arr2[j]
#         print(sums, end=' ')

# # Maximum from two arrays

# a1 = [1, 2, 3]
# a2 = [5, 6, 7]
# mx = 0

# n = len(a1)
# m = len(a2)

# for i in range(n):
#     for j in range(m):
#         s = a1[i] + a2[j]
#         mx = max(mx, s)

# print(s)

# # Triplet sum

# list = [1, 2, 3, 4, 5, 6]
# n = len(list)

# for i in range(0, n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             s = list[i]+list[j]+list[k]
#             print(s, end = ' ')

# # Prime numbers in range

# a = 0
# b = 10

# prime_count = 0

# for i in range(a, b+1):
#     count = 0
#     for j in range(1, i+1):
#         if (i%j == 0):
#             count += 1

#     if(count == 2):
#         prime_count += 1

# print(prime_count)

# n = 10
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=' ')
#     print()

n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print('*', end=' ')
    for j in range(2*n+1):
        print('*', end=' ')
    for j in range(n-i-1):
        print('*', end=' ')
    print()
