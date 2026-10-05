#Total Sales by City.Grouping 
sales = [
    {"city": "Mumbai", "amount": 15000},
    {"city": "Pune", "amount": 8000},
    {"city": "Mumbai", "amount": 12000},
    {"city": "Delhi", "amount": 18000},
    {"city": "Pune", "amount": 10000}
]

total_amount = 0
sales_by_city = {}

for sale in sales:
    city = sale["city"]
    amount = sale["amount"]
    
    if city not in sales_by_city:
        sales_by_city[city] = 0
    
    sales_by_city[city] += amount
    total_amount += amount
    
for city, amount in sales_by_city.items():
    print(f"City : {city} | Amount : {amount:.2f}") 
    
    
print(f"Overall_Amount : {total_amount:.2f}")   

