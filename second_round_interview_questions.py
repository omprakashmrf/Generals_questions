from collections import deque

input_rule = {')': '(', ']': '[', '}': '{'}

def is_valid(s: str) -> bool:
    stack = deque()
    
    for char in s:
        if char in input_rule.values():  # opening brackets
            stack.append(char)
        elif char in input_rule:         # closing brackets
            if not stack or stack.pop() != input_rule[char]:
                return False
        else:
            # If any invalid character is present
            return False
    
    return not stack  # True if stack is empty

# Test cases
print(is_valid("[{()}]"))      # True
print(is_valid("[()()]{}"))    # True
print(is_valid("([]"))         # False
print(is_valid("([{]})"))      # False


def get_longest_increasing_seq(nums):
    num_set = set(nums)
    longest_seq = []

    for num in num_set:
        if num - 1 not in num_set:  # potential start of a sequence
            current = num
            temp_seq = [current]

            while current + 1 in num_set:
                current += 1
                temp_seq.append(current)

            if len(temp_seq) > len(longest_seq):
                longest_seq = temp_seq

    return longest_seq

# Test examples
print(get_longest_increasing_seq([1, 2, 3]))                         # [1, 2, 3]
print(get_longest_increasing_seq([1, 2, 2]))                         # [1, 2]
print(get_longest_increasing_seq([1, 2, 3, 2, 9, 10, 11, 12, 13, 6, 7, 8]))  # [9, 10, 11, 12, 13]


#include <stdio.h>

int main() {
    int a = 5, b = 10;

    // Swap without third variable
    a = a + b;  // a = 15
    b = a - b;  // b = 5
    a = a - b;  // a = 10

    printf("a = %d, b = %d\n", a, b);
    return 0;
}

a = 5
b = 10

a, b = b, a

print(a, b)  # Output: 10 5


Q 4 there are 8 bolls all looks identical one of then slightly heavier then the others. find heavy one using
Optimal Strategy: Use Divide and Compare

🔁 Step-by-step:
Step 1: Divide into 3 groups

Group A: 3 balls
Group B: 3 balls
Group C: 2 balls
Step 2: Weigh Group A vs Group B

If equal, heavy ball is in Group C (the 2 remaining balls)
➤ Weigh the 2 balls: 1 more weighing → Find heavier one
✅ Total weighings = 2
If not equal, heavier group has the heavy ball
➤ Take 3 balls from heavier group → Go to next step
Step 3: Weigh 2 balls from the heavier group

If equal, the 3rd is heavier
If not equal, heavier one is the heavy ball
✅ Total weighings = 2
✅ Final Answer:

You can always find the heavy ball with just 2 weighings.
def find_heavy_ball(balls):
    # balls is a list of 8 weights, one of which is heavier
    group1 = balls[:3]
    group2 = balls[3:6]
    group3 = balls[6:]

    if sum(group1) == sum(group2):
        return 6 if balls[6] > balls[7] else 7
    elif sum(group1) > sum(group2):
        group = group1
        base = 0
    else:
        group = group2
        base = 3

    if group[0] == group[1]:
        return base + 2
    elif group[0] > group[1]:
        return base + 0
    else:
        return base + 1

# Example usage:
balls = [1, 1, 1, 1, 1, 1, 1, 2]  # heavy ball at index 7
print("Heavy ball index:", find_heavy_ball(balls))


synchronous programming 
def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 finished")

def task2():
    print("Task 2 started")

task1()
task2()

Asyncronous programing 
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())


| Feature         | **Django**                     | **Flask**                     | **FastAPI**                               |
| --------------- | ------------------------------ | ----------------------------- | ----------------------------------------- |
| Type            | Full-stack framework           | Microframework                | Modern, async web framework               |
| Release Year    | 2005                           | 2010                          | 2018                                      |
| Async Support   | Limited (partial in Django 3+) | No (until Flask 2.0+)         | ✅ Excellent async support                 |
| Performance     | Moderate                       | Fast                          | ⚡ Very Fast (near Node.js)                |
| Learning Curve  | Steeper                        | Beginner-friendly             | Moderate (requires some typing knowledge) |
| Best For        | Large, structured apps         | Small to medium APIs/web apps | Modern APIs, async-heavy apps             |
| Built-in Admin  | ✅ Yes                          | ❌ No                          | ❌ No                                      |
| Data Validation | ❌ Manual or forms              | ❌ Manual                      | ✅ Automatic (via Pydantic)                |
| Routing Style   | Declarative, class-based       | Function-based                | Function + decorator + typing             |



#map() implementation 

map(func, iterable)
                                                                                                
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]

result = my_map(square, nums)

# Since it's a generator, convert to list
print(list(result))  # Output: [1, 4, 9, 16, 25]


                                                                                                

                                                                                                








