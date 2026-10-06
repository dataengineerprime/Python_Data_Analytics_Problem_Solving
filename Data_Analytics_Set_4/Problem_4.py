# Find the average purchase amount for each city.
purchases = [
    {"city": "Mumbai", "amount": 10000},
    {"city": "Pune", "amount": 8000},
    {"city": "Mumbai", "amount": 20000},
    {"city": "Pune", "amount": 12000},
]

total_amount_city = {}
count_for_city = {}

for purchase in purchases:
    city = purchase["city"]
    amount = purchase["amount"]
    
    if city not in count_for_city:
        count_for_city[city] = 0
        total_amount_city[city] = 0
        
    total_amount_city[city] += amount
    count_for_city[city] += 1
    
for city in total_amount_city:
    average_amount = (total_amount_city[city] / count_for_city[city])
    print(city, average_amount)   
