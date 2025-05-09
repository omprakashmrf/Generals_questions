1. height anf infront questions

def reconstruct_queue(Height, Infront):
    people = list(zip(Height, Infront))
    
    # Sort by height descending, infront ascending
    people.sort(key=lambda x: (-x[0], x[1]))
    
    queue = []
    for height, infront in people:
        queue.insert(infront, height)  # Insert person at the index = infront count
    return queue

# Example usage
Height = [5, 3, 2, 6, 1, 4]
Infront = [0, 1, 2, 0, 3, 2]

print(reconstruct_queue(Height, Infront))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# remove nth node from singly linked list 
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy

    # Move fast n+1 steps to maintain gap
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the target node
    slow.next = slow.next.next

    return dummy.next

# find the kth element from tree ds 
def kthSmallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

# find the valid paranthesis 
def longestValidParentheses(s):
    stack = [-1]
    max_len = 0

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len




