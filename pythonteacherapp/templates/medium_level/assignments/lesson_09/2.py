employees = []
employee = {'name': 'John', 'age': 30, 'salary': 50000}
employees.append(employee)
employee = {'name': 'Kumar', 'age': 28, 'salary': 70000}
employees.append(employee)
employee = {'name': 'Methma', 'age': 31, 'salary': 100000}
employees.append(employee)

print("Current employees:")
print(employees)
print()


for employee in employees:
    if employee['name'] == 'Kumar':
        found_employee = employee
        break
    
if found_employee:
    employees.remove(found_employee)

print("Updated employees:")
print(employees)
print()