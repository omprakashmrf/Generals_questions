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
