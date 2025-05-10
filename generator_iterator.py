In Python, a generator is a simple and powerful tool for creating iterators. They allow you to generate values on the fly using yield, which helps save memory and makes your code more readable for streaming data or large sequences.

A generator is a function that yields values one at a time using yield instead of returning all values at once using return.

def fibonociiseries(n):
    a, b = 0,1
    
    count = 0
    while count < n:
        yield a
        a,b = b, a+b
        count +=1

for num in fibonociiseries(10):
    print(num)

 # How yield Works (vs return)
def count_up_to(n):
    for i in range(1, n + 1):
        yield i

# Create generator object
counter = count_up_to(5)

print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# Practical Use Case: File Line Reader
def read_large_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

for line in read_large_file('sample.txt'):
    print(line)


