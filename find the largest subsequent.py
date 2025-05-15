def largestsubs(s):
    char_set = set()
    
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1    
            
        char_set.add(s[right])
        
        max_len = max(max_len,right-left+1)
    print(max_len)
    return max_len        

largestsubs("length of the longest substring without repeating characters")



def longest_unique_substring(s):
    start = 0
    max_len = 0
    used_chars = {}
    longest = ""

    for i, char in enumerate(s):
        if char in used_chars and used_chars[char] >= start:
            start = used_chars[char] + 1
        used_chars[char] = i
        if i - start + 1 > max_len:
            max_len = i - start + 1
            longest = s[start:i+1]

    return longest

# Example
s = "abcabcbb"
print("Longest unique substring:", longest_unique_substring(s))

