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

#brute fore 
def longest_k_size_brute(s, k):
    max_len = 0
    for i in range(len(s)):
        char_set = set()
        for j in range(i, len(s)):
            char_set.add(s[j])
            if len(char_set) <= k:
                max_len = max(max_len, j - i+1)
            else:
                break;
    return max_len    
s="eceba"
k = 2      
print(longest_k_size_brute(s, k))  

# optimal sol
def longest_k_size(s, k):
    if len(s)< k:
        return 0
    char_map = {}
    max_len = 0
    left =0
    
    for right in range(len(s)):
        char=s[right]
        
        char_map[char]=char_map.get(char, 0)+1
        
        while len(char_map) >k:
            left_char=s[left]
            
            char_map[left_char] -=1
            if char_map[left_char]==0:
                del char_map[left_char]
            left +=1    
            
        max_len=max(max_len, right -left +1)    
        
    return max_len   
s="eceba"
k = 2        
print(longest_k_size(s, k))  
      
