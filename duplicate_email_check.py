customers = [
    {"name": "Rahul Sharma", "email": "Rahul@gmail.com", "city": "Mumbai"},
    {"name": "Priya Shah", "email": "priya@gmail.com", "city": "Pune"},
    {"name": "Rahul Sharma", "email": " rahul@gmail.com ", "city": "Mumbai"},
    {"name": "Amit Patil", "email": "amit@gmail.com", "city": "Mumbai"},
    {"name": "Priya Shah", "email": "PRIYA@GMAIL.COM", "city": "Pune"}
]

unique_emails = set()
duplicate_customers = []

for customer in customers:
    customer["email"] = customer["email"].strip().lower()
    
    name = customer["name"]
    email = customer["email"]
    
    if email in unique_emails:
        if name not in duplicate_customers: #if email repeats more than 2 times.
            duplicate_customers.append(name)
        
      
    else:
        unique_emails.add(email)

    
print(duplicate_customers)
