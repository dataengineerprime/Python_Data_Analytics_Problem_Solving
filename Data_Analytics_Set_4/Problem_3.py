employees = [
    {"name": "Amit", "department": "IT", "salary": 60000},
    {"name": "Neha", "department": "HR", "salary": 50000},
    {"name": "Rahul", "department": "IT", "salary": 80000},
    {"name": "Sneha", "department": "HR", "salary": 70000},
    {"name": "Karan", "department": "IT", "salary": 70000}
]

total_salary = 0
total_employee = 0
salary_by_employees = {}
employee_by_department = {}

for employee in employees:
    department = employee["department"]
    salary = employee["salary"]
    
    if department not in employee_by_department:
        employee_by_department[department] = 0
        
    if salary not in salary_by_employees:
        salary_by_employees[salary] = 0
        
    salary_by_employees[salary += salary
    total_salary += salary
    
    employee_by_department[department] += 1
