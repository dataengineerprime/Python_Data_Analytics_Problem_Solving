#Cleaning city and email
customers = [
    {"name": "Rahul Sharma", "email": " Rahul@Gmail.com ", "city": "Mumbai", "purchase": 15000},
    {"name": "Priya Shah", "email": "priyagmail.com", "city": "Pune", "purchase": 8000},
    {"name": "Amit Patil", "email": "", "city": "Mumbai", "purchase": -500},
    {"name": "Sneha Joshi", "email": "sneha@gmail.com", "city": " Mumbai ", "purchase": 18000},
    {"name": "Karan Mehta", "email": "karan@gmail.com", "city": "Pune", "purchase": 22000}
]

for customer in customers:
    customer["city"] = customer["city"].strip().title()
    customer["email"] = customer["email"].strip().lower()
    print(customer)
