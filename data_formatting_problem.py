customers = [
    {"name": "Rahul Sharma", "email": "Rahul@Gmail.com", "city": "Mumbai", "purchase": 15000},
    {"name": "Priya Shah", "email": "priyagmail.com", "city": "Pune", "purchase": 8000},
    {"name": "Amit Patil", "email": "", "city": "Mumbai", "purchase": -500},
    {"name": "Sneha Joshi", "email": "sneha@gmail.com", "city": "", "purchase": 18000},
    {"name": "Karan Mehta", "email": "karan@gmail.com", "city": "Pune", "purchase": 22000}
]

data_quality_issues = []


for customer in customers:
    email = customer["email"]
    city = customer["city"]
    purchase = customer["purchase"]
    name = customer["name"]
    
    has_issues = False
    
    if email == "":
        print(f"Missing email address: {name}")
        has_issues = True
    
    if city == "":
        print(f"Missing city name: {name}")
        has_issues = True
    
    if email != "" and ("@" not in email or not email.endswith(".com")):
        print(f"Invalid email format: {name}")
        has_issues = True
        
    if purchase < 0:
        print(f"Invalid purchase amount: {name}")
        has_issues = True
    
    if has_issues:
        data_quality_issues.append(name)
    else:
        print(f"No data quality issues: {name}")
        
print(f"Customers with data quality issue: {data_quality_issues}")        
    
    

        

