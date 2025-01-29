a = [2,4,8,22,44,66]
b = 9
index = 3
lenth = len(a)
if lenth==index:
    a = a[:index]+ [b]

else:
    a = a[:index]+ [b]+ a[index:]
    
print(a[:2])
