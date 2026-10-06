#Average Salary by department.
employees = [
    {"name": "Amit", "department": "IT", "salary": 60000},
    {"name": "Neha", "department": "HR", "salary": 50000},
    {"name": "Rahul", "department": "IT", "salary": 80000},
    {"name": "Sneha", "department": "HR", "salary": 70000},
    {"name": "Karan", "department": "IT", "salary": 70000}
]

salary_by_department = {}
employee_count_by_department = {}

for employee in employees:
    department = employee["department"]
    salary = employee["salary"]

    if department not in salary_by_department:
        salary_by_department[department] = 0
        employee_count_by_department[department] = 0

    salary_by_department[department] += salary
    employee_count_by_department[department] += 1


for department in salary_by_department:
    average_salary = (
        salary_by_department[department]
        / employee_count_by_department[department]
    )

    print(f"{department} → Average Salary: {average_salary:.2f}")
