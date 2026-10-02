customers = [
    {"name": " Rahul Sharma ", "email": "Rahul@Gmail.com", "city": "Mumbai", "purchase": 15000},
    {"name": "Priya Shah", "email": "priyagmail.com", "city": " Pune ", "purchase": 8000},
    {"name": "Amit Patil", "email": "", "city": "Mumbai", "purchase": -500},
    {"name": "Sneha Joshi", "email": "sneha@gmail.com", "city": " Mumbai ", "purchase": 18000},
    {"name": "Karan Mehta", "email": "karan@gmail.com", "city": "Pune", "purchase": 22000},
    {"name": "Rahul Sharma", "email": " rahul@gmail.com ", "city": "Mumbai", "purchase": 12000}
]


invalid_customers = []
valid_purchase_total = 0

for customer in customers:
    
    customer["name"] = customer["name"].strip().title()
    customer["email"] = customer["email"].strip().lower()
    customer["city"] = customer["city"].strip().title()
    
    name = customer["name"]
    email = customer["email"]
    city = customer["city"]
    purchase = customer["purchase"]
    
    has_issues = False
    
    
    if email == "":
        print(f"Missing Email Address: {name}")
        has_issues = True
        
    if email != "" and ("@" not in email or not email.endswith(".com")):
        print(f"Invalid email format: {name}")
        has_issues = True
        
    if purchase < 0:
        print(f"Invalid purchase amount: {name}")
        has_issues = True
    
    if not has_issues:
        valid_purchase_total += customer["purchase"] #Accumulator
        
    if has_issues:
        invalid_customers.append(name)
    else:
        print(f"No data quality issues: {name}")  
              
        
print(f"Valid Purchase Total: {valid_purchase_total:.2f}") 
print(f"Invalid Customers: {invalid_customers}")
         
        
    
