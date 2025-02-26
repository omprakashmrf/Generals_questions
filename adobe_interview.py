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
