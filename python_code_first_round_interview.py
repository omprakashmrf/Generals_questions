1. No, you cannot use a list as a key in a dictionary in Python.

Why?
Dictionary keys must be hashable — meaning they have a fixed hash value and are immutable. Lists are mutable, so they are not hashable and cannot be used as dictionary keys.

Example:
my_list = [1, 2, 3]
my_dict = {my_list: "value"}  # ❌ This will raise a TypeError
Error:
TypeError: unhashable type: 'list'
Alternative:
1. We have list and using that list as key in dictionary it will work?
If you need to use a collection of values as a key, you can use a tuple (which is immutable and hashable) instead:

my_list = [1, 2, 3]
my_dict = {tuple(my_list): "value"}  # ✅ This works
print(my_dict)
Would you like help refactoring some code that tries to use lists as keys?


2. You said:
Create one class, and objects (obj1, obj2) of the class, then use obj1 and obj2 as key in dictionary      it will work or not?
ChatGPT said:
Yes, using objects of a class as dictionary keys will work by default in Python.

Why?
Python class instances are hashable by default unless you override their __hash__ or __eq__ methods in a way that breaks that. Their default hash is based on their id() (memory address), which makes them usable as dictionary keys.

Example:
class MyClass:
    def __init__(self, value):
        self.value = value

obj1 = MyClass(10)
obj2 = MyClass(20)

my_dict = {
    obj1: "Object 1",
    obj2: "Object 2"
}

print(my_dict[obj1])  # Output: Object 1
print(my_dict[obj2])  # Output: Object 2
✅ This works fine.

Important Note:
Two different objects with the same data are still different keys unless you override __eq__ and __hash__.
obj3 = MyClass(10)
print(obj3 == obj1)  # False, unless __eq__ is overridden
print(obj3 in my_dict)  # False
Would you like an example where we override __eq__ and __hash__ so that objects with the same value are treated as equal keys?

You said:
2. what is hashable 
ChatGPT said:
What is Hashable in Python?
An object is hashable if:

It has a hash value that does not change during its lifetime.
It can be used as a key in a dictionary or stored in a set.
It implements __hash__() and __eq__() properly.
Examples of Hashable Types (✅):
int, float, str, bool
tuple (only if it contains only hashable elements)
frozenset
None
User-defined objects (by default)
hash("hello")       # ✅ Works
hash(123)           # ✅ Works
hash((1, 2, 3))     # ✅ Works
Examples of Unhashable Types (❌):
list
dict
set
hash([1, 2, 3])     # ❌ TypeError: unhashable type: 'list'
Why Hashability Matters:
Hashable objects can be used as keys in dictionaries and elements in sets:

my_dict = { (1, 2): "a tuple" }  # ✅ tuple is hashable
my_set = { "apple", "banana" }  # ✅ str is hashable
Unhashable types cannot be used in this way because they can change, which would break the way sets and dictionaries organize data.

Let me know if you want a visual explanation or how to make your custom object hashable.

You said:
3. ATM machine amount break down problem,      input = amount = 3300, we have note of [500,200,100],     output = print("note of 500 is  6)                     print("note of 200 is  1)                     print("note of 100 is  1)
ChatGPT said:
Here's a simple Python program to solve the ATM amount breakdown problem using the available notes [500, 200, 100].

✅ Problem:
Input: amount = 3300
Available notes: 500, 200, 100
Goal: Find out how many notes of each denomination are needed (starting from the largest) to make up the amount.
✅ Code:
def atm_breakdown(amount):
    notes = [500, 200, 100]
    for note in notes:
        count = amount // note
        if count > 0:
            print(f"Note of {note} is {count}")
            amount %= note

# Example usage
atm_breakdown(3300)
✅ Output:
Note of 500 is 6
Note of 200 is 1
Note of 100 is 1
This works by:

Using the largest note possible first (greedy approach),
Then subtracting the used amount from the total,
Continuing with the next smaller denomination.
Let me know if you want this adapted for user input or with error checking.

4. You said:
What is multithreading
ChatGPT said:
🧵 What is Multithreading in Programming?
Multithreading is a technique where a program runs multiple threads (smaller units of a process) at the same time (concurrently). Each thread represents a separate path of execution — like doing multiple tasks at once within a single program.

✅ Key Concepts:
A thread is a lightweight sub-process.
Multithreading allows multiple operations (like reading a file, downloading data, processing input) to run concurrently.
Useful for I/O-bound tasks (e.g., network calls, file access), not for CPU-heavy tasks in Python due to the Global Interpreter Lock (GIL).
🧠 Analogy:
Imagine a kitchen (a program) where:

One cook (thread) chops vegetables,
Another cook (thread) boils water,
A third cook (thread) preps the stove.
All tasks happen in parallel, improving efficiency.

🛠️ Python Example:
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for ch in 'ABCDE':
        print(f"Letter: {ch}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()
📌 Output:
You'll see numbers and letters printed interleaved, since both threads run simultaneously.

⚠️ Note About Python:
Due to the Global Interpreter Lock (GIL):

Threads don’t run in true parallel for CPU-bound tasks.
Use multiprocessing module for heavy computations.
Multithreading is still great for I/O-bound tasks (e.g., file, network, database).
Would you like to see an example comparing multithreading and multiprocessing?

5. You said:
What is hashing?
ChatGPT said:
🔐 What is Hashing?
Hashing is the process of converting data (like a string, number, or file) into a fixed-size value called a hash code or hash value, usually using a mathematical function called a hash function.

🧠 Think of it like:
Turning any input — "apple" or 1234 — into a short fingerprint (e.g., 23fjsk9a) that represents the data.

✅ Key Properties of Hashing:
Deterministic: Same input always gives the same output.
Fast: Quickly converts data to a hash.
Fixed Output Size: Output size is the same regardless of input size.
Efficient Comparison: Easier to compare hash values than full data.
Hard to Reverse: A good hash function should not allow reversing the hash to get the original input.
🔧 Example in Python:
print(hash("apple"))      # Outputs an integer (e.g., 587216345...)
print(hash(12345))        # Outputs an integer
(Note: Python’s hash() output may differ between sessions for security.)

📦 Real-World Uses of Hashing:
Use Case	Purpose
Dictionaries/Sets	Hashing is used to quickly find keys.
Password Storage	Passwords are stored as hashes for security.
File Integrity	Check if a file has changed (e.g., with SHA256 hash).
Data Structures	Hash tables, hash maps, etc.
🔐 Example: Hashing a Password (One-Way Hash)
import hashlib

password = "mypassword123"
hashed = hashlib.sha256(password.encode()).hexdigest()
print(hashed)
Output:

a4b615bc7e8d...  # 64-character hex string
⚠️ Hashing ≠ Encryption
Hashing is one-way (you can't reverse it).
Encryption is two-way (you can decrypt the original).
Would you like an example showing how hashing helps with dictionaries or password storage?

6. You said:
suppose we have string "my name is shubham" find 2nd largest word.
ChatGPT said:
To find the 2nd largest word in the string "my name is shubham", follow these steps:

✅ Step-by-step plan:
Split the string into words.
Sort the words by length in descending order.
Pick the second item.
🛠️ Code:
text = "my name is shubham"

# Step 1: Split into words
words = text.split()

# Step 2: Sort by length in descending order
words_sorted = sorted(words, key=len, reverse=True)

# Step 3: Get the 2nd largest word
if len(words_sorted) >= 2:
    print("2nd largest word:", words_sorted[1])
else:
    print("Not enough words")
🧾 Output:
2nd largest word: name
Words: ["my", "name", "is", "shubham"]
Sorted by length: ["shubham", "name", "my", "is"]
2nd largest = "name"
Let me know if you want it to handle duplicate lengths or return all second-largest words!

7. You said:
 What is GIL?
ChatGPT said:
🧵 What is GIL (Global Interpreter Lock) in Python?
The GIL (Global Interpreter Lock) is a mechanism used in CPython (the standard implementation of Python) that allows only one thread to execute Python bytecode at a time, even on multi-core systems.

🚧 Why Does GIL Exist?
CPython’s memory management (especially garbage collection) is not thread-safe.
GIL was introduced to simplify memory management by avoiding complex thread synchronization issues.
🔍 What It Means:
In a multi-threaded Python program, even if you create multiple threads, only one thread executes Python code at a time.
Other threads are paused — they wait for the GIL to be released.
📌 Example Problem:
import threading

def count():
    for i in range(1000000):
        pass

t1 = threading.Thread(target=count)
t2 = threading.Thread(target=count)

t1.start()
t2.start()
t1.join()
t2.join()
Even with two threads, this won’t fully utilize multiple CPU cores because of the GIL. It runs almost like single-threaded code.

✅ When GIL is Not a Problem:
For I/O-bound tasks (like file operations, web requests), GIL doesn’t hurt much because threads release the GIL during I/O.
Example: Web scraping, downloading files, reading/writing files.
❌ When GIL is a Problem:
For CPU-bound tasks (like complex calculations), threads can’t truly run in parallel, even on multi-core CPUs.
Solution: Use multiprocessing module instead of threading.
🛠️ How to Bypass GIL for CPU Tasks:
from multiprocessing import Process

def compute():
    for i in range(10**7):
        pass

p1 = Process(target=compute)
p2 = Process(target=compute)

p1.start()
p2.start()
p1.join()
p2.join()
This uses separate processes — each with its own Python interpreter and GIL — allowing real parallelism.

🔁 Summary:
Aspect	GIL Behavior
Purpose	Simplifies memory safety
Affects	Only CPython (not Jython, IronPython)
Limits	Multi-threaded CPU-bound performance
Alternatives	Use multiprocessing for CPU tasks
Let me know if you want a visual explanation or benchmark comparison!

8. You said:
What is race condition?
ChatGPT said:
⚠️ What is a Race Condition?
A race condition is a type of bug that occurs in multi-threaded or multi-process programs when two or more threads access shared data at the same time, and the final outcome depends on the timing of how those threads are scheduled.

🧠 Simple Analogy:
Imagine two people trying to withdraw money from the same bank account at the same time:

Both check the balance (e.g., $100),
Both see $100 and decide it's safe to withdraw $70,
Both withdraw, resulting in -$40, which is incorrect.
🔧 Python Example (with Race Condition):
import threading

balance = 100

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print(f"Withdrawn {amount}, Remaining: {balance}")
    else:
        print("Insufficient funds")

# Create two threads that access the shared variable
t1 = threading.Thread(target=withdraw, args=(70,))
t2 = threading.Thread(target=withdraw, args=(70,))

t1.start()
t2.start()
t1.join()
t2.join()
📉 Possible Outputs:
Withdrawn 70, Remaining: 30
Withdrawn 70, Remaining: -40   ← ❌ Race condition!
This happens because:

Both threads read balance at the same time,
They both believe it's safe to withdraw.
✅ How to Prevent Race Conditions:
Use locks or synchronization mechanisms to ensure that only one thread can access the shared resource at a time.

lock = threading.Lock()

def safe_withdraw(amount):
    global balance
    with lock:  # Acquire and release automatically
        if balance >= amount:
            balance -= amount
            print(f"Withdrawn {amount}, Remaining: {balance}")
        else:
            print("Insufficient funds")
🔁 Summary:
Feature	Description
Race Condition	Bug caused by unsynchronized access to shared data
Occurs in	Multithreading / multiprocessing
Risk	Inconsistent or incorrect results
Fix	Use locks (e.g., threading.Lock()) or other synchronization tools
Would you like to see a version with the lock added or a visual explanation of what's going wrong?

9. You said:
Create class and create 2 thread use count in class and increment by one     thread one call 5 times     thread two call 15 time      what will be output in the last ? with Implementation
ChatGPT said:
Great question! You're exploring shared data access with threads in Python. Let's walk through:

🧾 Goal:
Create a class with a shared count variable.
Use 2 threads:
Thread 1 calls increment() 5 times.
Thread 2 calls increment() 15 times.
At the end, print the final value of count.
🔴 Without Lock (Possible Race Condition):
import threading
import time

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        current = self.count
        time.sleep(0.001)  # simulate a small delay
        self.count = current + 1

# Create counter object
counter = Counter()

# Define thread functions
def thread_one():
    for _ in range(5):
        counter.increment()

def thread_two():
    for _ in range(15):
        counter.increment()

# Create threads
t1 = threading.Thread(target=thread_one)
t2 = threading.Thread(target=thread_two)

# Start and join threads
t1.start()
t2.start()
t1.join()
t2.join()

print("Final count:", counter.count)
🧯 Possible Output:
Final count: 18   ✅ (correct)
Final count: 17   ❌ (race condition)
Final count: 16   ❌
Final count: 19   ❌
Because increment() is not atomic, both threads can interfere with each other's updates to self.count.

✅ With Lock (Thread-Safe Version):
import threading
import time

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            current = self.count
            time.sleep(0.001)  # simulate delay
            self.count = current + 1

counter = Counter()

def thread_one():
    for _ in range(5):
        counter.increment()

def thread_two():
    for _ in range(15):
        counter.increment()

t1 = threading.Thread(target=thread_one)
t2 = threading.Thread(target=thread_two)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final count:", counter.count)
✅ Guaranteed Output:
Final count: 20
Because the lock ensures only one thread updates count at a time, preventing race conditions.

Would you like to see this example extended with multiple counters or logging each step of execution?

11. You said:
If you have 50 gb file and this file has 3 lines which has my name yash how to print that 3 lines in python.
ChatGPT said:
Great question! When dealing with a very large file (e.g., 50 GB), you should not load the entire file into memory. Instead, use streaming (line-by-line reading).

✅ Goal:
Print all lines from a large file that contain the name "yash".

✅ Efficient Python Solution (Memory-Safe):
# Replace 'your_file.txt' with the path to your 50 GB file
with open("your_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "yash" in line:
            print(line.strip())
🧠 Why This Works:
Reads the file one line at a time.
Uses minimal memory, regardless of file size.
Only prints lines containing "yash".
🔍 Enhancements (Optional):
If case-insensitive match is needed:

if "yash" in line.lower():
Or to collect the 3 lines instead of printing:

matched_lines = []
with open("your_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "yash" in line:
            matched_lines.append(line.strip())
            if len(matched_lines) == 3:
                break

print(matched_lines)
Let me know if the file is compressed, binary, or stored remotely (like on S3 or HDFS) — I can help with that too!

12. You said:
a = 10        def func(a):              a = a+10              print(a)         print(a)         func(a)        print(a) 
ChatGPT said:
Let's walk through the Python code step by step and explain what happens:

🔢 Code:
a = 10

def func(a):
    a = a + 10
    print(a)

print(a)
func(a)
print(a)
🔍 Explanation:
a = 10: Global variable a is initialized to 10.
print(a): Prints the global a, which is 10.
func(a):
Passes the value of a (which is 10) into the function.
Inside the function, a is local to the function.
a = a + 10 makes local a = 20.
print(a) prints the local value, which is 20.
print(a) again outside the function still prints 10, because the global a hasn't changed.
🖨️ Output:
10
20
10
🧠 Key Concept:
Function parameters are passed by value (for immutable types) in Python. Reassigning a inside the function does not affect the global a.

Let me know if you want the same example for mutable types (like lists), where behavior is different!

14. You said:
what will be output ? a = [1,2,3] def func(a):      a.append(10)      print(a)   print(a)   
ChatGPT said:
Let's analyze your Python code:

🧾 Code:
a = [1, 2, 3]

def func(a):
    a.append(10)
    print(a)

print(a)
🧠 Key Concept:
Lists are mutable objects in Python.
When you pass a list to a function, you're passing a reference to the original list — not a copy.
So if you modify the list (e.g., with append()), it changes the original list.
🖨️ Output:
[1, 2, 3]
Why?

You defined the function func(a) but never called it, so the list remains unchanged.
Only print(a) outside the function runs.
✅ If You Add func(a):
a = [1, 2, 3]

def func(a):
    a.append(10)
    print(a)

print(a)
func(a)
print(a)
Output would be:
[1, 2, 3]
[1, 2, 3, 10]
[1, 2, 3, 10]
Because:

First print(a) shows the original list.
func(a) modifies it (adds 10).
Final print(a) shows the updated list.
Let me know if you want the behavior with a = a + [10] inside the function — it behaves differently!

15. You said:
what is frozenset
ChatGPT said:
❄️ What is a frozenset in Python?
A frozenset is an immutable version of a set.
Once created, you cannot change a frozenset — no adding or removing elements.

✅ Key Features:
Feature	set	frozenset
Mutable	Yes	No
Hashable	No	Yes
Can be a dict key	No	Yes
Unordered	Yes	Yes
Duplicate-free	Yes	Yes
🧪 Example:
# Normal set
s = set([1, 2, 3])
s.add(4)           # Works

# Frozenset
fs = frozenset([1, 2, 3])
# fs.add(4)        ❌ AttributeError: 'frozenset' object has no attribute 'add'
print(fs)
Output:

frozenset({1, 2, 3})
🔒 Why Use frozenset?
To prevent modification of a set.
To use a set as a dictionary key or as an element of another set, which requires elements to be hashable.
a = frozenset([1, 2])
b = frozenset([3, 4])

d = {a: "first", b: "second"}
print(d[frozenset([1, 2])])  # ✅ Works!
⛔ Invalid Operations on frozenset:
These will raise errors:

fs.add(5)      # ❌
fs.remove(1)   # ❌
✅ Valid Operations:
You can still use methods like:

union()
intersection()
difference()
issubset()
len(), in
📌 Summary:
frozenset is like a read-only set.
Useful when you need a set that should never change.
Allows sets to be used in places where immutability is required, like keys in dictionaries.
Let me know if you'd like to see how frozenset compares in performance or use cases like caching or graph edges!

You said:
basic python coding questions 
ChatGPT said:
Here are some basic Python coding questions — perfect for beginners or interview practice. I've grouped them by topic and included example problems.

🔢 1. Numbers and Math

Q1. Write a program to check if a number is even or odd.

num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
Q2. Find the factorial of a number.

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
🧮 2. Lists

Q3. Find the largest number in a list.

nums = [3, 9, 5, 2]
print(max(nums))
Q4. Remove duplicates from a list.

nums = [1, 2, 2, 3, 3]
unique = list(set(nums))
print(unique)
📜 3. Strings

Q5. Check if a string is a palindrome.

s = "madam"
print(s == s[::-1])
Q6. Count vowels in a string.

s = "hello world"
count = sum(1 for c in s if c.lower() in "aeiou")
print(count)
🔁 4. Loops

Q7. Print numbers from 1 to 10 using a loop.

for i in range(1, 11):
    print(i)
Q8. Print a pattern:

*
**
***
for i in range(1, 4):
    print("*" * i)
🧠 5. Functions and Conditions

Q9. Write a function to check if a number is prime.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
📂 6. Files

Q10. Read a file and print all lines containing the word "error".

with open("log.txt", "r") as file:
    for line in file:
        if "error" in line:
            print(line.strip())
📦 Bonus: Dictionary

Q11. Count frequency of each character in a string.

s = "hello"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print(freq)
Would you like a quiz format or practice problems to solve on your own with answers later?

You said:
collection module 
ChatGPT said:
The collections module in Python is a built-in library that provides specialized container datatypes — alternatives to the built-in dict, list, set, and tuple. It's very useful for cleaner, faster, and more readable code.

📦 Common Types in collections Module:

1. Counter
Counts frequency of elements in an iterable (like a list or string).

from collections import Counter

data = ['a', 'b', 'a', 'c', 'b', 'a']
count = Counter(data)
print(count)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})
2. defaultdict
Like a normal dictionary, but gives a default value for missing keys.

from collections import defaultdict

dd = defaultdict(int)  # Default value is 0
dd['apple'] += 1
print(dd['apple'])   # Output: 1
print(dd['banana'])  # Output: 0 (not error)
You can also use:

dd = defaultdict(list)  # Default value is []
dd['x'].append(10)
3. namedtuple
Creates tuple-like objects with named fields for readability.

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)       # Output: 3 4
print(p)              # Output: Point(x=3, y=4)
4. deque (Double-Ended Queue)
A list-like container with fast appends and pops from both ends.

from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)             # Output: deque([0, 1, 2, 3, 4])
dq.pop()              # Removes 4
dq.popleft()          # Removes 0
5. OrderedDict (Deprecated in Python 3.7+)
Used to remember the insertion order of keys.
Note: In Python 3.7+, regular dict preserves order by default.

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)  # Output: OrderedDict([('a', 1), ('b', 2)])
✅ Summary Table

Type	Purpose
Counter	Count frequency of items
defaultdict	Auto default for missing keys
namedtuple	Tuples with named fields (like mini-objects)
deque	Double-ended queue (efficient list ops)
OrderedDict	Dict that remembers insertion order
Would you like real-world use cases, interview questions, or a quiz based on these?

You said:
how to sort dict
ChatGPT said:
In Python, you can sort a dictionary in two main ways:

✅ 1. Sort by Keys

data = {'b': 2, 'a': 1, 'c': 3}

sorted_by_keys = dict(sorted(data.items()))
print(sorted_by_keys)
🖨️ Output:

{'a': 1, 'b': 2, 'c': 3}
✅ 2. Sort by Values

data = {'b': 2, 'a': 1, 'c': 3}

sorted_by_values = dict(sorted(data.items(), key=lambda item: item[1]))
print(sorted_by_values)
🖨️ Output:

{'a': 1, 'b': 2, 'c': 3}
🔄 3. Sort in Reverse (Descending)

🔁 By Values:
sorted_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print(sorted_desc)
📋 Note:

sorted() returns a list of tuples (key-value pairs).
Wrapping it in dict() gives you a sorted dictionary.
From Python 3.7+, dictionaries maintain insertion order — so the sorted order is preserved.
💡 Extra: Sort dictionary by length of value string
data = {'apple': 'red', 'banana': 'yellow', 'kiwi': 'green'}

sorted_custom = dict(sorted(data.items(), key=lambda item: len(item[1])))
print(sorted_custom)
Would you like to sort a nested dict, or sort only keys or only values?

# Your team owns a Django-based Orders service that powers business-critical APIs. Support has reported that some endpoints respond slowly at random times, and the tech lead wants execution-time logging added to suspect functions. The rule: the business logic inside those functions must not be touched — the instrumentation has to be reusable across any function in the codebase.
# Question
# a) First, write a plain decorator log_execution_time that logs the function's name and its execution time in milliseconds. It must work with any function signature, must return the function's result, and must not break the decorated function's name or docstring.
# b) Now upgrade the same decorator to accept a parameter threshold_ms — it should log only when execution time exceeds the threshold.
# Code provided:
# def fetch_orders(customer_id, status="OPEN"):
#     """Returns open orders for a customer."""
#     ...  # existing business logic — do not modify

# solution a).
import time    
    
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res=func(*args, **kwargs)
        excution_time  = time.time() - start_time
        print(f"{func.__name__} ecution_time {excution_time}")
        return res
    return wrapper

@log_execution_time
def say():
    print("this is sample function")

say()


# solution b)
def log_execution_time(func):
    def wrapper(thresold_ms = 0):
        start_time = time.time()
        res=func(*args, **kwargs)
        excution_time  = time.time() - start_time
        if excution_time > thresold_ms:
            print(f"{func.__name__} ecution_time {excution_time}")
        return res
    return wrapper

Student  ---> name, id, address, school_name, subject
API----> 

POST http/ api/students. 
APIVIew
---

get ---> api/students/{id}
create student 

GET. 


def decorator(func):
    def wrapper(id, name):
        print(f"hello {name}")
        res=func(id, name)
        return res
    return wrapper    


@decorator
def student(id, name ):
    print(id, name)
    
student(1, "omprakash")  

list1 =[1,[2,[3,4,[5]]]]

def flatternlist(lst):
    result = []
    
    for item in lst:
        if isinstance(item, list):
            result.extend(flatternlist(item))
        else:
            result.append(item)
    return result

print(flatternlist(list1))        


# Imagine you are processing a massive stream of log data from a server. You have a massive list (or stream) of strings where each string represents a log line.
# Write a python function called extract_ errors(log_stream) that iterates over this stream. 
# If a line contains the substring 'ERROR', it should yield a dictionary 
# containing the log level and the message. Ignore all other log levels.



def ertract_logs(log_string):
    # result = []
    for line in  log_string:
        if "ERROR" in line:
            parts=line.split(" ", 2)
            #print((parts[2]))
            #print(parts)
            yield {
                    "log level": parts[0],
                    "message": parts[1] +" "+ parts[2]  
                }
    #return result        

logs = [
"INFO: Server started successfully",
"ERROR: Database connection timeout",
"DEBUG: Loaded 40 items",
"ERROR: Disk space critical"
]

# logs = [
# "ERROR: Server started successfully for id: 1234"
# ]

for error in ertract_logs(logs):
    print(error)

class Solution:
    def reverseWords(self, s: str) -> str:
        if s is None:
            return s
        words=s.split()
        reverse=words[::-1]
        output = ""
        for word in reverse:
            output +=  word + " "
            print(word) 
        print(output.strip())  

class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        reverse=words[::-1]
        return " ".join(reverse)


obj= Solution()
s= "my name is omprakash"
print(obj.reverseWords(s))

# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcdxyzxb"
# Output: 7
# Explanation: The answer is "abcdxyz", with the length of 7.
# Example 2:
# Input: s = "abcdabcbbxyzt"
# Output: 5
# Explanation: The answer is "bxyzt", with the length of 5.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a subs
#tring.

def longest_substring(s):
    longest = 0
    char_index ={}
    left = 0

    for right, ch in enumerate(s):
        if ch in char_index and char_index[ch] >=left:
            left = char_index[ch] + 1
        char_index[ch] = right

        longest = max(longest, right - left +1)
    return longest 

s = "abcdabcbbxyzt"
print(longest_substring(s))
