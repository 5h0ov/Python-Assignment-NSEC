name = input("Enter the names of the employee  separated by spaces: ").split()
salary = input("Enter the salaries of the employee respectively separated by spaces: ").split()

# Create a dictionary by combining the two lists
employee_dict = dict(zip(name, salary))

print()
print(employee_dict)
