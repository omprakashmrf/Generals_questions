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

0 => aa0
1 => aa1
2 => aa2
3 => aa3
4 => aa4
5 => aa5
6 => aa6
7 => aa7
8 => aa8
9 => aa9
10 => ab0
11 => ab1

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
        flattened.extend(flater(item))
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


def longest_substring(s):
    start= max_len=0
    char_index = {}
    longest = ""
    
    for i, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= start:
            start = char_index[ch] +1
        
        char_index[ch] =i    
        
        if (i-start+1) > max_len:
            max_len = i- start+1
            longest = s[start:i+1]
    
    
    return max_len, longest


print(longest_substring("abcabcbb")) 


def squared(f):
    def wrapper(self, *args, **kwargs):
        result = f(self, *args, **kwargs)
        result=result**2
        return (result)
    return wrapper   
 
# ---- Do not Change ----- #
class Operations:
    @squared
    def multiply(self, a,b):
        return a*b
 
 
print(f"Res is {Operations().multiply(1,2)}")
 
print(f"Res is {Operations().multiply(-1,2)}")  

a=[
    {
        "name": "tom",
        "score": 40
    },
        {
        "name": "sam",
        "score": 80
    },
        {
        "name": "max",
        "score": 70
    }
]

b=sorted(a, key=lambda x:x["score"])
print(b[-1]["name"])
    
a=[1,2,4,1,4,1,2,5,6,2,1,5,3,5,6]   
a.sort()
b = set(a)
c=list(b)
print(c[-2])


a=[
    {
        "name": "tom",
        "score": 40
    },
        {
        "name": "sam",
        "score": 80
    },
        {
        "name": "max",
        "score": 70
    }
]
def find_name(b):
    max_score=a[0]["score"]
    for i in a:
        if i["score"] > max_score:
            max_score = i["score"]
            name = i["name"]
    
    return name


print(find_name(a))

from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i


a=[1, 2, [3,4], [5,6]]

def flattern(lst):
    result = []
    #print(lst)
    for item in lst:
        if isinstance(item, list):
            result.extend(flattern(item))
        else:
            result.append(item)
    return result
print(flattern(a))   

Input="aabbccfd"
#Result=f
# Result =d
from collections import Counter
def non_repetable(a):
    count=Counter(a)
    for i in count:
        if count[i]==1:
            print(i)
            break;
            
        

(non_repetable(Input))  

NLU, RASAtold, dilogflow methods framework  


def find_mean_and_median(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    
    # Calculate mean
    mean = sum(merged) / n
    
    # Calculate median
    if n % 2 == 0:
        median = (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        median = merged[n // 2]
    
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    return mean, median

# Test
nums1 = [2, 3, 4, 5]
nums2 = [4, 5, 6, 7]
find_mean_and_median(nums1, nums2)

Capgemini 
1. 
correct ans 
a = ["a", "a", "b", "b", "c", "c", "c", "a", "a"]

output = ""
count = 1

for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        count += 1
    else:
        output += a[i - 1] + str(count)
        count = 1  # reset count

# Add the last group
output += a[-1] + str(count)

print(output)  # Output: a2b2c3a2


2. 
a = [[1,2,3], [[4,5,[6]]], [7]]
output=[1,2,3,4,5,6,7]

def flattern(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flattern(item))
        else:
            result.append(item)
            
    return result

print(flattern(a))

2. col_a, col_b
1   	1
2   	0
1   	NULL
0   	1



3. Employee table

Emp_No	Emp_Name	Salary	Location	Dept_No

101		Graham		10345	New York	40

102		Mike		20436	Toranto		30

103		Dean		15730	Mexico		60

104		John		10000	New York	40

105		Sara		25000	New York	40
 
Department Table:

Dept_No	Dept_Name

30		Sales

40		Marketing

50		Audit


SELECT Emp_Name, Salary
FROM Employee e
JOIN Department d ON e.Dept_No = d.Dept_No
WHERE d.Dept_Name = 'Marketing'
ORDER BY Salary DESC
OFFSET 1 ROW
FETCH NEXT 1 ROW ONLY;

important questions
1. solid principals 
2. design pattern 
3. sequence of thread, process, task, etc
4. asynchronous process
5. how to finds the aws file is uploaded on s3 bucket 
6. how to deploy aws lambda in function on aws 
7. what is aws endpoint.
8. what is Async await 


1. Write a function to count the number of unique digits in a number - eg 111 -> 1 121 -> 2 123 -> 3


from collections import Counter
input = "11122221"
count=Counter(input)
print(count)
print(len(count))

 2. Write a function to return the longest even length word in a sentence.
 Sample input: Be not afraid of greatness, some are born great, some achieve greatness, and some have greatness thrust upon them.
  output -> 
input="Be not afraid of greatness, some are born great, some achieve greatness, and some have greatness thrust upon them."

a=input.split()
a.sort(key=len)

print(a)
max_len_word = 0
for i in a:
    if len(i) %2==0:
        max_len_word = max(len(i), max_len_word)

print(max_len_word) 


3. Program to flatten the list 
Input=[1,[2,3, [4, 5]]] 
# Output = [1,2,3,4,5]

def flatten(arr):
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print(flatten(Input))  

4. We have a table called BookAuthor. It has two columns Book and Author, Book being unique column. Write a query to find the names of the authors who have written more than 10 books.

book_list=BookAuthor.object.filter(author="Om").count() > 10

6. Given a List of n integers and a number k, find the pairs of numbers in the list such that the difference between the pair is k. 
Find the optimal solution with and without extra storage.

taget = k
pair = (1,2) = 1-2

Pwc internal interview questions --->
1.  manipulated same list without taking extra var 
# Original list
nums = [3, 1, 4, 2, 2, 3, 1, 4, 5, 6]
print("Original:", nums)

# ✅ 1. Remove duplicates in-place (preserve order)
seen = set()
nums[:] = [x for x in nums if not (x in seen or seen.add(x))]
print("After removing duplicates:", nums)

# ✅ 2. Remove even numbers in-place
nums[:] = [x for x in nums if x % 2 != 0]
print("After removing even numbers:", nums)

# ✅ 3. Double each element in-place
for i in range(len(nums)):
    nums[i] *= 2
print("After doubling elements:", nums)

# ✅ 4. Sort the list in-place
nums.sort()
print("After sorting:", nums)

# ✅ 5. Reverse the list in-place
nums.reverse()
print("After reversing:", nums)



2.  convert list into tuple ()
nums = [1, 2, 3, 4]
nums = tuple(nums)  # Now nums is a tuple
print(nums)         # Output: (1, 2, 3, 4)


3. can i use same var tuple as var for store
you can, but don't use its bad practice 

: - Great question — if you use a built-in name (like list, dict, tuple, str, etc.) as a variable, the main problem is 
that you override or shadow the original built-in function. This can lead to unexpected errors and broken code later.

4. if key is not prasent in dict how we can handle without error 

    Use .get() Method (Safest)
    my_dict = {"a": 1, "b": 2}
    value = my_dict.get("c", 0)  # returns 0 if key 'c' not found
    print(value)  # Output: 0
    🔹 .get(key, default) returns the value if key exists, otherwise returns default (or None if not provided)

5. mutable and unmutable data set in python and group them

| Category  | Types                                                                |
| --------- | -------------------------------------------------------------------- |
| Mutable   | `list`, `dict`, `set`, `bytearray`, `defaultdict`, `deque`           |
| Immutable | `int`, `float`, `bool`, `str`, `tuple`, `frozenset`, `bytes`, `None` |


def merge_sorted_arrays(a, b):
    i, j = 0, 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    # Add remaining elements
    c.extend(a[i:])
    c.extend(b[j:])

    return c

# Example
a = [10, 20, 30]
b = [20, 35, 40, 45]
c = merge_sorted_arrays(a, b)
print(c)  # Output: [10, 20, 20, 30, 35, 40, 45]


def merge_and_sort_brute(a, b):
    c = a + b  # Step 1: Combine
    n = len(c)

    # Step 2: Brute-force sort (Bubble Sort)
    for i in range(n):
        for j in range(0, n - i - 1):
            if c[j] > c[j + 1]:
                c[j], c[j + 1] = c[j + 1], c[j]  # Swap

    return c

# Example
a = [10, 20, 30]
b = [20, 35, 40, 45]
c = merge_and_sort_brute(a, b)
print(c)  # Output: [10, 20, 20, 30, 35, 40, 45]

def decorator(func):
    def inner(a, b):
        try:
            result=func(a, b)
        except Exception as e:
            result = None
            return (f"b should not be zero {e}")
        return result    
    return inner    
        

@decorator
def divide(a, b):
    return a/b
    
print(divide(4, 2))   

Example: Immutable Type (int behaves like call by value)
def modify_number(x):
    x = x + 10
    print("Inside function:", x)

a = 5
modify_number(a)
print("Outside function:", a)

output
Inside function: 15
Outside function: 5


Example: Mutable Type (list behaves like call by reference)
def modify_list(lst):
    lst.append(100)
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)

output 
Inside function: [1, 2, 3, 100]
Outside function: [1, 2, 3, 100]


nested_list = [1, [2, [3, 4], 5], [2], [4,[3,4,5,[1]]], 8]


def flattern_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flattern_list(item))
        else:
            result.append(item)
    return result
print(flattern_list(nested_list))    

funcs = [lambda x: x*i for i in range(5)]
#print(funcs)
for f in funcs:
    print(f(2))

res = [f(2) for f in funcs]

print(res)

not a ans [0, 2, 4, 6, 8]

In Python, closures capture variables by reference, not by value. This means all the lambdas refer to the same variable i, and it will be evaluated when the function is called, not when it's defined. 
ans =[8,8,8,8]

How to Fix It (Capture i at Definition Time)
If you want each function to remember its own value of i, you can use a default argument trick:
funcs = [lambda x, i=i: x*i for i in range(5)]
 
