# Sample set
my_set = {3, 1, 4, 1, 5, 9}

# Sorting the set by converting it to a list
sorted_list = sorted(my_set)

# Output the sorted list
print("Sorted set (as a list):", sorted_list)

# If you want to convert the sorted list back to a set (note: it will lose order in the set)
sorted_set = set(sorted_list)
print("Sorted set (as a set):", sorted_set)

# Sorting the set in reverse order
sorted_set_desc = sorted(my_set, reverse=True)

# Output the sorted set in reverse
print("Sorted set (descending order):", sorted_set_desc)



# Sample tuple
my_tuple = (3, 1, 4, 1, 5, 9)

# Convert the tuple to a list and sort it
sorted_list = sorted(my_tuple)

# Convert the sorted list back to a tuple
sorted_tuple = tuple(sorted_list)

# Output the sorted tuple
print("Sorted tuple:", sorted_tuple)

# Sorting the tuple in reverse order
sorted_tuple_desc = tuple(sorted(my_tuple, reverse=True))

# Output the sorted tuple in reverse
print("Sorted tuple (descending):", sorted_tuple_desc)


data = {
    'b': 2,
    'a': 1,
    'd': 4,
    'c': 3
}

print(data.items())
c=dict(sorted(data.items()))
print(c)

result = []
for k,v in sorted(data.items()):
    result.append(k)
    

print(result)







data = {
    'Name': ['Ram', 'Shyam', 'Geeta', 'Pooja', 'Anshika'],
    'Age': [25, 15, 35, 40, 20],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Andaman'],
    'Salary': [50000, 60000, 55000, 70000, 65000]
}

# print(data)

sal_list=data['Salary']
# print(sal_list)

sal_list=sorted(sal_list)
print(sal_list)
b=sal_list[-2]
print(b)

c=data['Salary'].index(b)
print(c)

result = {k: data[k][c]  for k in data}
print(result)







employees = [
    {"name": "John", "salary": 5000},
    {"name": "Jane", "salary": 7000},
    {"name": "Doe", "salary": 6000},
    {"name": "Smith", "salary": 8000}
]

# Sort the list by salary in descending order and get the second item
sorted_employees = sorted(employees, key=lambda x: x['salary'], reverse=True)

second_highest_salary = sorted_employees[1]  # The second highest salary object

print("Second highest salary:", second_highest_salary)



my_dict = {'c': 3, 'a': 1, 'b': 2}

# Sorting by keys
sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}

print(sorted_dict)
