a = [12,3,27, 5, 4, 4, 9, 4 ]
result = 180
for i in range(len(a)-2):
    for j in range(len(a)-1):
        k = result/(a[i]*a[j])
        
        if k in a[i+2:]:
            print(a[i], a[j], k)
