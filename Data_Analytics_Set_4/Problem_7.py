#What is the average completed sales for each region?
sales = [
    {"employee": "Amit", "region": "West", "sales": 45000, "status": "Completed"},
    {"employee": "Neha", "region": "North", "sales": 32000, "status": "Pending"},
    {"employee": "Rahul", "region": "West", "sales": 60000, "status": "Completed"},
    {"employee": "Sneha", "region": "South", "sales": 28000, "status": "Completed"},
    {"employee": "Karan", "region": "North", "sales": 52000, "status": "Completed"},
    {"employee": "Priya", "region": "West", "sales": 38000, "status": "Cancelled"}
]


average_sales_by_region = {}

completed_sales_by_region = {}
completed_count_by_region = {}

for sale in sales:
    region = sale["region"]
    amount = sale["sales"]

    if sale["status"] == "Completed":
        if region not in completed_sales_by_region:
            completed_sales_by_region[region] = 0
            completed_count_by_region[region] = 0

        completed_sales_by_region[region] += amount
        completed_count_by_region[region] += 1
    

for region in completed_sales_by_region:
    average_sales = (
        completed_sales_by_region[region] / completed_count_by_region[region]
    )

    average_sales_by_region[region] = average_sales

print(average_sales_by_region)
