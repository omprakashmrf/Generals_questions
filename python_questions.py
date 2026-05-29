my_dict = {'c': 3, 'a': 1, 'b': 2}
# Sorting by keys
sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}
print(sorted_dict)


# converting interger into decimal
import decimal
interger=10
a=decimal.Decimal(interger)
print(a)
print(type(a))

# converting string into decimal
string="123456"
b = decimal.Decimal(string)
print(b)
print(type(b))


# reverse string using slice 
main_string="python programming"
reverse_string=main_string[::-1]
print(reverse_string)

# count the vawel
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count=0

for i in range(len(word)):
    if word[i] in vowel:
        count+=1
print(count)

# count the consonant in the word
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count=0

for i in range(len(word)):
    if word[i] not in vowel:
        count+=1
print(count)


# found the number of occurence
word= "python"
charactor = "p"
count=0

for i in word:
    if i==charactor:
        count+=1
print(count)     

# find the max number in list
aa=[3,44,6,8]
max_number = aa[0]
for i in aa:
    if max_number < i:
        max_number = i
        
#max_number=max(aa)
print(max_number)


aa=[3,44,6,8]
min_number = aa[0]
for i in aa:
    if min_number > i:
        min_number=i
        
#min_number=max(aa)
print(min_number)


# find the middle element in the list 
ll=[3,6,80,9,12]
middleplace = int(len(ll)//2)
value=ll[middleplace]
print(value)

# converting list into string 
bb=['3','5','7','8','9']

print("".join(bb))



#max_number=max(aa)
print(max_number)


aa=[3,44,6,8]
min_number = aa[0]
for i in aa:
    if min_number > i:
        min_number=i
        
#min_number=max(aa)
print(min_number)


# find the middle element in the list 
ll=[3,6,80,9,12]
middleplace = int(len(ll)//2)
value=ll[middleplace]
print(value)

# converting list into string 
bb=['3','5','7','8','9']
print("".join(bb))


# check anagram 
str1="Listen"
str2="silent"

abc=list(str1.upper())
cde=list(str2.upper())
abc.sort()
cde.sort()

if abc==cde:
    print(True)
else:
    print(False)

# check polindrom
str1 = "kayak".lower()
str2 = "kayak".lower()

if str1==str2[::-1]:
    print(True)
else:
    print(False)
    

#count spaces in the string     
string = "P r ogramm in g "
print(string.count(" "))

#count space and char and number 
import re 
name = 'Python is 1'
#count_dict = {"char": [], }
digitcount=re.sub("[^0-9]", "", name)
lettercount= re.sub("[^a-zA-Z]", "", name)
spacecount = re.findall("[ \n]", name)
print(len(digitcount), len(lettercount), len(spacecount))
#for i in name:


# find all special charactor    
import re
spChar = "!@#$%^&*()"
allspchar=re.sub("[\w]", "", spChar)
print(len(allspchar))    


string ="C O D E"
spaces = re.compile(r'\s+')
sss=re.sub(spaces, "", string)
print((sss))

floor = 3
h = floor*2-1

for i in range(1, floor*2, 2):
    print(("{:^{}}").format('*'*i, h))

from random import shuffle
lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)
    

# Write a program to identify the missing numbers in the sequence without using any loop.
seq = [1,2,3,4,6,7,8,9,14,15]

num=set(range(min(seq), max(seq)+1)) - set(seq)
print(num)

# Write a simple logic using multiple decorators to print list of words in lower case
 
input1="Hello World"
# Output: ["hello", "world"]
 
# You main method should take the input and all the functionality done by the decorators( 1 for splitting the words and 1 for lowering the case)

def to_lower_case(func):
    def wrapper(text):
        # for word in text:
        res=func(text.lower())
        # print(type(res))
        return res
    return wrapper

def split_text(func):
    def wrapper(text):
        res=func(text)
        return res.split()
    return wrapper
    
    

@to_lower_case
@split_text
def simple_input(s):
    return s

print(simple_input(input1))   

# Write a Python function that finds all unique permutations of a given list of integers, including duplicates. The function should return these permutations as a list of lists without using inbuilt function.
 
# input_list = [1, 1, 2]
 
# # Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
# def get_permutation(nums):
#     result = []
    
#     def back_track():
#         if 

# Design a simple banking system with the following requirements:
 
# Create a BankAccount class that includes:
 
# A public method to display account details.
# A protected method to calculate interest (for subclasses).
# A private method to validate the account number.
# Create a subclass called SavingsAccount that inherits from BankAccount. The SavingsAccount class should:
 
# Have an additional attribute for the interest rate.
# Override the protected method to calculate interest based on the balance and interest rate.
# Implement a way to display account details that includes the calculated interest.

class BankAccount:
    def __init__(self, account_number, acount_name, balance):
        self.account_number = account_number
        self.acount_name = acount_name
        self.balance = balance
    
    # private method
    def __validate_account_number(self):
        if not (sel.account_number).isdigit():
            raise valueError("invalid account")
    
    def _calculate_interest(self):
        "calculatre logic need to write here "
        return "interest logic"
    
    def display_account_details(self):
        print("account number", self.account_number)
        print("account holder name", self.account_name)
        print("account balance", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, interest_rate, account_number, acount_name, balance):
        super().__init__(account_number, acount_name, balance)
        
        self.interest_rate = interest_rate
        
    def _calculate_interest(self):
        return ""
        
    def display_account(self):
    

a =[1, 2, 3]
squre_number = list(map(lambda x: x**2, a))
print(squre_number)


#  Employees

# | emp_id | name    | dept_id | salary | manager_id |

# | ------ | ------- | ------- | ------ | ---------- |

# | 1      | Alice   | 10      | 60000  | NULL       |

# | 2      | Bob     | 20      | 50000  | 1          |

# | 3      | Charlie | 10      | 40000  | 1          |

# | 4      | David   | 30      | 45000  | 2          |

# | 5      | Eva     | 20      | 55000  | 1          |
 
# Departments

# | dept_id | dept_name |

# | ------- | --------- |

# | 10      | HR        |

# | 20      | IT        |

# | 30      | Finance   |
 
# q. a) Find employees who earn more than their manager salary


select e.emp_id,
        e.name AS emplyee name
        m.name AS manager_name
        From Employees e
    JOIN Employees m
    On e.manager_id = m.emap_id 
    where m.salary < e.salary

# Write a Pandas query to find the top 5 products by sales.

top_five_records=df.sort_value(by="sales", accending=False).head(5)


d = {"om": {"eng": 45, "math": 56, "sci": 32}, "Prakash": {"eng": 76, "math": 43, "sci": 84}, "Yadav": {"eng": 23, "math": 48, "sci": 53}}

for key, value in  d.items():
    # print(key, value)
    #print(type(value))
    sorted_dict=dict(sorted(value.items(), key=lambda x:x[1]))
    print(sorted_dict)
    #print(key, value)

def decorator(func):
    def wrapper(text):
        res=func(text)
        return res.upper()
    return wrapper    

@decorator
def f(x):
 return x
 
r = f("yadav")
 
print(r)

import json 
data = {"name": "om", "age": 30}
json_data = json.dump(data)
print(json_data)

class User(model.models):
    name = models.charFields(max_len=20)
    age = models.IntergerFields():

select * from User where name ="om"
try:
    qs=User.objects.get(name=name)  
except User.Doesnotexist:
    qs = None
from flask import Flask, 

app =  Flask(__name__)

app.router("/add_user", method=["POST"])
def add_user(self, request):
    name = reques.get("name")

import threading
import time 

def text():
    print("for deplay", time.sleep(2))

t1=threading.Thread(target=text)   
t2= threading.Thread(target =text)

t1.start()
t2.start()

t1.join()
t2.join()

# Write a function which finds the sum of all odd digits and the sum of all even digits from a list of numbers.
# nums = [123, 456, 789, 10]

def sum_num(nums):
    odd_sum = 0
    even_sum = 0
    
    for i in nums:
        print(str(i))
        
        for digit in str(i):
            #print(type(digit))
            digit=int(digit)
            if digit % 2==0:
                even_sum +=digit
            else:
                odd_sum +=digit
    return odd_sum, even_sum            
print(sum_num(nums))


# what is the output of this code

a = [1, 2, 3, 4, 5, 6]
[1,0,3,0,5,0]

for i in range(len(a) - 1, -1, -2):
    print(i)
        
    a[i] = 0
print(a)
 
        
