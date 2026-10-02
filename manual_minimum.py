# A company wants to identify its lowest-value completed transaction.
transactions = [
    {"customer": "Amit", "amount": 25000, "status": "Completed"},
    {"customer": "Neha", "amount": 8000, "status": "Completed"},
    {"customer": "Rahul", "amount": 42000, "status": "Pending"},
    {"customer": "Sneha", "amount": 18000, "status": "Completed"},
    {"customer": "Karan", "amount": 55000, "status": "Completed"},
    {"customer": "Priya", "amount": 12000, "status": "Cancelled"},
    {"customer": "Rohan", "amount": 30000, "status": "Completed"}
]

lowest_amount_transaction = None
lowest_customer_name = None

for transaction in transactions:
    if transaction["status"] == "Completed":
        
        if lowest_amount_transaction is None:
            lowest_amount_transaction = transaction["amount"]
            lowest_customer_name = transaction["customer"]
        
        elif transaction["amount"] < lowest_amount_transaction:
            lowest_amount_transaction = transaction["amount"]
            lowest_customer_name = transaction["customer"]
        
print(f"Lowest amount: {lowest_amount_transaction}")
print(f"Customer: {lowest_customer_name}")
    
#This was tough for me.

            
    
    


