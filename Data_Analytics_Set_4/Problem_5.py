sales = [
    {"city": "Mumbai", "amount": 15000},
    {"city": "Pune", "amount": 8000},
    {"city": "Mumbai", "amount": 25000},
    {"city": "Delhi", "amount": 18000},
    {"city": "Pune", "amount": 22000},
    {"city": "Delhi", "amount": 12000}
]

highest_average = 0
highest_average_city = None
total_city_amount = {}
count_of_city = {}

for sale in sales:
    city = sale["city"]
    amount = sale["amount"]
    
    
    if city not in count_of_city:
        count_of_city[city] = 0
        total_city_amount[city] = 0
        
    total_city_amount[city] += amount
    count_of_city[city] += 1
    
for city in total_city_amount:
    average_amount = total_city_amount[city] / count_of_city[city] 
    
    if average_amount > highest_average:
        highest_average = average_amount
        highest_average_city = city
        
print("City:", highest_average_city)
print("Average Sales:", highest_average)
    
    
