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

#. problem --> find the sum of min len sub array eqaul to s
# approch --> add one one element into the window and moving farword 
# and checking len is greater or equal to S
# deleting the the element from left 
# and incrementing the left pointer
# and maintaining the min_len of window 
def min_len_sum_subarry(arr, s):
    min_len= float('inf')
    left=0
    window_sum=0
    
    
    for right in range(len(arr)):
        window_sum +=arr[right]
    
        while window_sum >= s:
            min_len=min(min_len, right-left+1)
            window_sum-=arr[left]
            left+=1
    
    return min_len if min_len != float('inf') else 0

arr=[3,5,7,8,9,1]
s=8
print(min_len_sum_subarry(arr, s))    

# find the permutations of given two string

from collections import Counter
def getpermutation(s1, s2):
    len1, len2 = len(s1), len(s2)
    
    if len1 > len2:
        return False
    
    count1=Counter(s1)
    window = Counter(s2[:len1])
    
    if count1 == window:
        return True
    
    for i in range(len1, len2):
        window[s2[i]] +=1
        
        window[s2[i - len1]] -=1
        
        if window[s2[i-len1]]==0:
           del window[s2[i-len1]]
        
        if window==count1:
            return True
    return False

s1 ="ab"
s2 ="eidbbaoo"

print(getpermutation(s1, s2))    
output--> True


class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    
def reverse_linkedlist(head):
    prev = None
    curr = head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        
        prev = curr
        curr = nxt
    return prev

def print_list(head):
    curr = head
    while curr:
        print(curr.val,  end=" --> ")
        curr = curr.next
    print(None)

    
# create linked list 1-->2-->3-->4-->None

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)

head = Node(10)
#printlinked list
print_list(head)

reverse_list =(reverse_linkedlist(head))
4-->3-->2-->1-->None
print_list(reverse_list)


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cyclic(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(1)

print("Cycle present:", detect_cyclic(head))



head2 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head2.next = node2
node2.next = node3
node3.next = node4
# creating cycle: 4 → 2
node4.next = node2

print("Cycle present:", detect_cyclic(head2))


def merge_interval(intervals):
    intervals.sort(key=lambda x:x[0])   
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged 

intervals = [[1,3], [2,5], [6,8], [12, 15]]   
print(merge_interval(intervals))
output  = [[1, 5], [6, 8], [12, 15]]



from collections import OrderedDict

class LRUcache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key):
        if not key in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

lru = LRUcache(2)
lru.put(1, 1)
lru.put(2, 2)

print(lru.get(1))  # expected 1

lru.put(3, 3)      # removes key 2

print(lru.get(2))  # expected -1

lru.put(4, 4)      # removes key 1

print(lru.get(1))  # -1
print(lru.get(3))  # 3
print(lru.get(4))  # 4           
            
        
