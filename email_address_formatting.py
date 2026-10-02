customers = [
    {"name": "Rahul Sharma", "email": "Rahul@Gmail.com", "city": "Mumbai", "purchase": 15000},
    {"name": "Priya Shah", "email": "priyagmail.com", "city": "Pune", "purchase": 8000},
    {"name": "Amit Patil", "email": "", "city": "Mumbai", "purchase": 12000},
    {"name": "Sneha Joshi", "email": "sneha@gmail.com", "city": "Delhi", "purchase": 18000},
    {"name": "Karan Mehta", "email": "karan@gmail.com", "city": "Pune", "purchase": 22000}
]

invalid_email_customers = []

for customer in customers:
    email = customer["email"]
    
    if email == "":
        print(f"Missing email address: {customer["name"]}")
        invalid_email_customers.append(customer["name"])
    elif "@" not in email:
        print(f"Missing @ in email: {customer["name"]}")
        invalid_email_customers.append(customer["name"])
    else:
        print("No formatting issue")
        

print(f"Customers with email address issues: {invalid_email_customers}")
