#Manager asks for 4 things
# 1. Clean the data
# Apply:
# name  → strip() + title()email → strip() + lower()city  → strip() + title()


# 2. Find invalid customers
# A customer is invalid if:
# - email is empty
# - email does not contain @
# - email does not end with .com
# - purchase is negative
# Store their names in:
# invalid_customers = []


# 3. Calculate total purchase from valid customers only
# Use:
# valid_purchase_total = 0


# 4. Find the highest valid purchase manually
# You must not use:
# max()


# Store:
# highest_purchase = Nonehighest_customer = None


# Also create a set of cities belonging to valid customers:
# valid_cities = set()


# Expected final information
# Your program should ultimately identify:
# Invalid customers
# Total valid purchase
# Highest valid purchase customer + amount
# Unique cities of valid customers
############################################################################Solution Below##################################

customers = [
    {"name": " Rahul Sharma ", "email": "Rahul@Gmail.com", "city": "Mumbai", "purchase": 15000},
    {"name": "Priya Shah", "email": "priyagmail.com", "city": "Pune", "purchase": 8000},
    {"name": "Amit Patil", "email": "", "city": "Mumbai", "purchase": -500},
    {"name": "Sneha Joshi", "email": "sneha@gmail.com", "city": " Mumbai ", "purchase": 18000},
    {"name": "Karan Mehta", "email": "karan@gmail.com", "city": "Pune", "purchase": 22000},
    {"name": "Rohan Mehta", "email": "rohan@gmail", "city": "Delhi", "purchase": 12000}
]

invalid_customers = []
valid_purchase_total = 0
highest_purchase = None
highest_customer = None
valid_cities = set()

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
        print(f"Missing email address: {name}")
        has_issues = True
    
    if email != "" and ("@" not in email or not email.endswith(".com")):
        print(f"Invalid email format: {name}")
        has_issues = True
        
    if purchase < 0:
        print(f"Negative purchase amount: {name}")
        has_issues = True
        
    if not has_issues:
        valid_purchase_total += purchase
        
        if highest_purchase is None or purchase > highest_purchase:
            highest_purchase = purchase
            highest_customer = name
        
            
        
        valid_cities.add(city)
        
    if has_issues:
        invalid_customers.append(name)
    else:
        print(f"No data quality issues: {name}")
        
  
print("Invalid customers:", invalid_customers)
print("Valid purchase total:", valid_purchase_total)
print("Highest purchase:", highest_purchase)
print("Highest customer:", highest_customer)
print("Valid cities:", valid_cities)

  
  
    
