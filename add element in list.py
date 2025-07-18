a = [2,4,8,22,44,66]
b = 9
index = 3
lenth = len(a)
if lenth==index:
    a = a[:index]+ [b]

else:
    a = a[:index]+ [b]+ a[index:]
    
print(a[:2])

a = ["a","a","b","b","c","c","c","a","a"]
output="a4b2c3"

output =""
from collections import Counter
b=Counter(a)
print(b)
seen = set()

for i in a:
    if i not in seen:
        output += f"{i}{b[i]}"
    seen.add(i)    
print(output) 


a = ["a","a","b","b","c","c","c","a","a"]
output="a2b2c3a2"
count = 1
output =""
for i in range(1, len(a)):
    if a[i] == a[i-1]:
        count +=1
    else:
        output +=f"{a[i -1]}{count}"
        count = 1 # reset count
output += a[-1] + str(count)   # adding last group     

print(output)    


import time
def decorator(func):
    def inner(*args, **kwargs):
        print(args)
        start_time=time.time()
        print("start time of the function", start_time)
        result=func(*args, **kwargs)
        print(result)
        end_time = time.time()
        print("end time of the function", end_time)
        if (end_time - start_time)  > 3:
            excution = end_time - start_time
        else:
            excution ="excution time is less then 2 sec"
        print(excution)
        return result
    return inner     
@decorator()
def sayhello():
    print("I want o find the excution time")
    
sayhello() 
import copy 

a = [2,4,6,8]
b=a.copy()
print(b)

c = copy.deepcopy(a)
c.append(10)
print(c)
print(a)


abc = [3,2,4, 6]
target = 10
Output: [1,2]

def getindex(nums):
    seen = {}
    for i, num  in enumerate(nums):
        diff = target - nums[i]
        if diff in seen:
            return [i, seen[diff]]
        seen[num] = i    
print(getindex(abc)) 

p= "aaabbbcc45aa"
# output= a3b3c245a2


def countsque(s):
    count=1
    output=""
    n = len(s)
    for i in range(1, n):
        if s[i-1] == s[i]:
            count +=1
        else:
            if not s[i-1].isdigit():    
                output +=s[i-1]+str(count)
            if s[i].isdigit():
                output += s[i]
            
            print(output)  
            count = 1
    output +=s[i]+str(count)   
    return output

print(countsque(p))  
