sliding window ---> problems

# # brute force approch 
def maxsumsubarr(arr, k):
    max_sum = 0
    for i in range(len(arr)-k +1):
        current_sum = sum(arr[i: i+k])
        max_sum = max(max_sum, current_sum)
        
    return max_sum
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(maxsumsubarr(arr, k))

# optimal solution

def max_sub_arr_sum(arr, k):
    if len(arr) < k:
        return None # not enough element for count
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum    
        
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sub_arr_sum(arr, k)) 
