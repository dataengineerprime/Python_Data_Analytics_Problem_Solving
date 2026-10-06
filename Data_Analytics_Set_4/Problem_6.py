#What is the total completed sales for each region?
sales = [
    {"employee": "Amit", "region": "West", "sales": 45000, "status": "Completed"},
    {"employee": "Neha", "region": "North", "sales": 32000, "status": "Pending"},
    {"employee": "Rahul", "region": "West", "sales": 60000, "status": "Completed"},
    {"employee": "Sneha", "region": "South", "sales": 28000, "status": "Completed"},
    {"employee": "Karan", "region": "North", "sales": 52000, "status": "Completed"},
    {"employee": "Priya", "region": "West", "sales": 38000, "status": "Cancelled"}
]

completed_sales_by_region = {}


for sale in sales:
    region = sale["region"]
    amount = sale["sales"]
    
    if sale["status"] == "Completed":
        if region not in completed_sales_by_region:
            completed_sales_by_region[region] = 0
            
        completed_sales_by_region[region] += amount
        
print(completed_sales_by_region)        
    
