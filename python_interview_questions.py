1. def generate_pattern(limit):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    count = 0

    for first in letters:
        for second in letters:
            for number in range(10):  # Numbers from 0 to 9 for each letter combination
                if count >= limit:
                    return
                print(f"{count} => {first}{second}{number}")
                count += 1

# Generate pattern up to 1000
generate_pattern(1000)

2. modulo operator

3. diffrent type of authentication in django

4. diffrent b/w jwt authentication and session authentication bearer token 

5. diffrentce b/w django and django rest framework

6. diffrence b/w MVT and MVC 
7. diffrence in  == and is operator in python

Q) # create flattered list
data = [1, 2, [3], 3, [4, 5]]
flattened = []

for item in data:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)

print(flattened)


Q) s = "yamini"
output="y1a1m1i2n1"
from collections import Counter

count = Counter(s)
output = ""
seen = set()

for i, char in enumerate(s):
    # If it's the last occurrence of the character
    if char not in seen:
        output += f"{char}{count[char]}"
        seen.add(char)

print(output)

# ATM machin cash withdrow
def atm_breakdown(amount):
    notes = [500, 200, 100]
    for note in notes:
        count = amount // note
        if count > 0:
            print(f"Note of {note} is {count}")
            amount %= note

# Example usage
atm_breakdown(3300)


SQL Query to Reverse the Values in a Column

UPDATE test_table
SET io = CASE 
            WHEN io = 1 THEN 0
            WHEN io = 0 THEN 1
         END;



# def prinmuber(num):
#     if num < 2:
#         return -1
    
#     result = []
#     is_prime=False
    
#     for i in range(num):
#         for j in range(2, int(num//2)):
#             if i%j==:
#                 break;
#             elif is_prime:
#                 result.append(j)

#     return result
# print(prinmuber(100))

class Account():
    def __init__(self, account):
        self.account=account
    
    def account_detail(self):
        #print("account class is calling")
        print(self.account)

class savingAccont(Account):
    
    def __init__(self, account_type):
        self.account_type=account_type
    
    def saving_acount(self):
        print(self.account_type)
        
class checking_account(Account):
    
    def __init__(self, account_balance):
        self.account_balance=account_balance
    
    def checking_acount(self):
        print(self.account_balance)
        return self.account_balance

        
d=checking_account(2000)
#print(d.account)
print(d.checking_acount())

# print(str("asdsfdsf"))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 101):
    if is_prime(num):
        print(num, end=' ')

def productexceptself(nums):
    n = len(nums)
    res = [1]*n
    
    prefix = 1
    for i in range(n):
        res[i]= prefix
        prefix *=nums[i]
        
    postfix = 1
    for i in range(n-1, -1, -1):
        res[i]*=postfix
        postfix *= nums[i]
    
    return res

print(productexceptself([1,2,3,4]))    

#with division oprator 
def productexceptself(nums):
    product =1
    zero_count = nums.count(0)
    res = []
    
    if zero_count >1:
        return [0]* len(nums)
    
    for num in nums:
        if num !=0:
            product *=num
    
    for num in nums:
        if zero_count==0:
            res.append(product//num)
        else:
            res.append(product if num==0 else 0)
        
    return res

print(productexceptself([1,2,3,4])) 


# inp_str = 'aaabbccca'
# output ='3a2b3c1a'

# # from collections import Counter

# # count = Counter(inp_str)
# # print(count)
# out=""
# seen = set()
# for i, ch in enumerate(inp_str):
#     if ch not in seen:
#         out +=f"{count[ch]}{ch}"
#         seen.add(ch)

# print(out)  

in_lst = [3,6,9,1,12,34,56,78,89]
inp_str = 'aaabbccca'
output ='3a2b3c1a'
in_lst.sort()
print(in_lst)
print(in_lst[1])


# import time

# def decorstor_func(func):
#     def wrapper():
#         start_time=time.time()
#         print("before calling the decoratore")
#         func()
#         excutation_time=time.time()-start_time
#         print(excutation_time)
#         print("after calling the decorator")
    
#     return wrapper     


# @decorstor_func
# def say():
#     print("this is my normal function")

# c = say()
# c
# a=(i for i in range(10) if i%2==0)

# print(next(a))
# print(next(a))
# print(next(a))

# def flator(b):
#     a= [1, [2, [3, 4], 5], 6]
#     for i in a:
#         if isinstance(i, list):
#             b.extend(i)
#             flator(b)
#         else:
#             b.append(i)
            

# print(flator())        

#output --> [1, 2, 3, 4, 5, 6]
# singlon class
# if large 
# monolathik and monololoc structure
# get and filter method
# MVC stucture
# micoservices
# multithreding and multiprocessing 
# how to implement multithreding 




