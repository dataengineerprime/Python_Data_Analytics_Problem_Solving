# How many customers are there in each city?

customers = [
    {"name": "Amit", "city": "Mumbai"},
    {"name": "Neha", "city": "Pune"},
    {"name": "Rahul", "city": "Mumbai"},
    {"name": "Sneha", "city": "Delhi"},
    {"name": "Karan", "city": "Pune"},
    {"name": "Priya", "city": "Mumbai"}
]

customer_by_city = {}

for customer in customers:
    city = customer["city"]
    
    if city not in customer_by_city:
        customer_by_city[city] = 0
        
    customer_by_city[city] += 1
    
for city, count in customer_by_city.items():
    print(f"City : {city} | Customers: {count}")
    
