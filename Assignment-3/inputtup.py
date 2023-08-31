empno = int(input("Enter Empno: "))
name = input("Enter Name: ")
salary = float(input("Enter Salary: "))

info = (empno, name, salary)

print("Entered Employee Information:")
print("Empno:", info[0])
print("Name:", info[1])
print("Salary:",info[2])
