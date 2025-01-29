def missingnumber(arr):
    n=len(arr)+1
    total_sum = (n*(n+1))//2
    print(total_sum)
    missinfnum = total_sum-sum(arr)
    print(missinfnum)
    return missinfnum

missingnumber([1,2,4,5,6])    

def is_palindrome(s):
    return s == s[::-1]

def reversearrayinplace(arr):
    left, right=0, len(arr)-1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        
        left +=1
        right -=1
    print(arr)
    return arr

reversearrayinplace([1,2,3,4,5,6]) 