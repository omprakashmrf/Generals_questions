Nearest Smaller Tower

def nearest_smaller_tower(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    # Nearest smaller to left
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(i)

    return result

# Example usage:
heights = [1, 3, 2, 4]
print(nearest_smaller_tower(heights))  # Output: [-1, 0, 0, 2]

Palindrome Score in a String



