def fibbonoci(n):
    if n <= 0:
        return []
    if n ==1:
        return [0]
    
    if n ==2:
        return [0, 1]
    
    series =[0,1]
    
    for i in range(2, n):
        series.append(series[-1]+ series[-2])
    
    return series

n  = int(input("enter the number of terms : "))
print("finnocii seriesn", fibbonoci(n))    


def fibbonacci():
    n = int(input("how many number you want to print . . ."))
    a = 0
    b = 1
    count =0
    if n < 0:
        print("Incorrect input")
    
    elif n==0:
        return 0
    
    elif n==1:
        return 1
        
    else:    
        print("fibbonacci series are . . .")
        
        while count < n:
            print(a)
            c = a+b
            a = b
            b = c
            count+=1
                        
print(fibbonacci())



