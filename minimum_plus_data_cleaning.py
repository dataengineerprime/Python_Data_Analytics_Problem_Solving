# Find the employee name and sales amount of the employee with the lowest sales among employees who:
# - are from the West region
# - met or exceeded their own target

sales_data = [
    {"employee": "Amit", "region": "West", "sales": 45000, "target": 40000},
    {"employee": "Neha", "region": "North", "sales": 32000, "target": 35000},
    {"employee": "Rahul", "region": "West", "sales": 60000, "target": 50000},
    {"employee": "Sneha", "region": "South", "sales": 28000, "target": 30000},
    {"employee": "Karan", "region": "North", "sales": 52000, "target": 45000},
    {"employee": "Priya", "region": "West", "sales": 38000, "target": 40000}
]

lowest_sales_employees = None
lowest_sales = None

for sales in sales_data:
    if sales["region"] == "West" and sales["sales"] >= sales["target"]:
        
        if lowest_sales is None:
            lowest_sales = sales["sales"]
            lowest_sales_employees = sales["employee"]
        
        elif sales["sales"] < lowest_sales:
            lowest_sales = sales["sales"]
            lowest_sales_employees = sales["employee"]
            
print(f"Lowest Sales Employees: {lowest_sales_employees}")            
print(f"Lowest Sales Amount: {lowest_sales:.2f}")            
            
    
