1. def generate_pattern(limit):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    count = 0

    for first in letters:
        for second in letters:
            for number in range(10):  # Numbers from 0 to 9 for each letter combination
                if count >= limit:
                    return
                print(f"{count} => {first}{second}{number}")
                count += 1

# Generate pattern up to 1000
generate_pattern(1000)

2. modulo operator

3. diffrent type of authentication in django

4. diffrent b/w jwt authentication and session authentication bearer token 

5. diffrentce b/w django and django rest framework

6. diffrence b/w MVT and MVC 
7. diffrence in  == and is operator in python

Q) # create flattered list
data = [1, 2, [3], 3, [4, 5]]
flattened = []

for item in data:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)

print(flattened)


Q) s = "yamini"
output="y1a1m1i2n1"
from collections import Counter

count = Counter(s)
output = ""
seen = set()

for i, char in enumerate(s):
    # If it's the last occurrence of the character
    if char not in seen:
        output += f"{char}{count[char]}"
        seen.add(char)

print(output)

# ATM machin cash withdrow
def atm_breakdown(amount):
    notes = [500, 200, 100]
    for note in notes:
        count = amount // note
        if count > 0:
            print(f"Note of {note} is {count}")
            amount %= note

# Example usage
atm_breakdown(3300)


SQL Query to Reverse the Values in a Column

UPDATE test_table
SET io = CASE 
            WHEN io = 1 THEN 0
            WHEN io = 0 THEN 1
         END;






