# WAF to print the length of list

cities = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bangalore', 'Pune']

def len_list(list):
    return len(list)

print(len_list(cities))

# Using for loop

def ele(list):
    for i in list:
        print(i, end=', ')

ele(cities)