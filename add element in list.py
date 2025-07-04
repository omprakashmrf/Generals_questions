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
output += a[-1] + str(count)        

print(output)        

