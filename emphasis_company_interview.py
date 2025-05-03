1 . What is Contaxt manager in python write custom contaxt manager


predefined context manager

with open("file.txt", "r") as f:
    data = f.read()


Here, Python:

Opens the file (__enter__)
Lets you work with it
Closes the file automatically (__exit__)

custom --->

class Mycontaxt:
    def __enter__(self):
        print("enter the contaxt")
        return "Resource ready"
    
    def __exit__(self, exe_type, exe_value, traceback):
        print("exiting the context")
        
        if exe_type:
            print(f"exception {exe_value}")
        return True

with Mycontaxt() as resource:
    print(resource)


another way

from contextlib import contextmanager

@contextmanager
def simple_context():
    print("Start")
    yield "Using Resource"
    print("End")

with simple_context() as val:
    print(val)


find longest substring length
def longestsubslen(s):
    a = set()
    left = 0
    max_len=0
    
    for right in range(len(s)):
        while s[right] in a:
            a.remove(s[left])
            left +=1
        a.add(s[right])
        max_len=max(max_len, right-left +1)
    
    return max_len  

find longest substring 

actual charactor
def longestsubstring(s):
    char_index = {}
    
    start = 0
    max_len = 0
    max_sub = ""
    
    for end, char in enumerate(s):
        # import pdb
        # pdb.set_trace()
        if char in char_index and char_index[char] >=start:
            start = char_index[char] +1
        char_index[char] = end
        
        if end - start+1 > max_len:
            max_len = end -start +1
            max_sub = s[start:end+1]
    
    return max_sub


def add(a, b):
    return a + b

import unittest
from your_module import add  # replace 'your_module' with your actual file name

class TestAddFunction(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
















