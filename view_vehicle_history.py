from datetime import datetime
import json
from data_handler import load_json

def load_transactions():
    transaction=load_json('data/transactions.json')
    return transaction

def search_by_date(start,end): 
    transaction=load_transactions() 
    day= []
    for i in transaction: 
        check_in_date=i['check_in'][:10]
        if start <= check_in_date <= end:
            day.append(i)
    for i in transaction:
        if i['check_out'] is not None:  
            check_out_date=i['check_out'][:10]
            if start<=check_out_date<=end:
                day.append(i)
        else:
            i['check_out'] = "Still Parked"
            day.append(i)
    return day

def display_transaction_history(start, end):
    transaction= search_by_date(start, end)
    if transaction==[]:
        print("No transactions found in this time period.")
    else:
        print(f"=== TRANSACTIONS FROM {start} TO {end} ===")
        for i in transaction:
            print(f"License Plate: {i['license_plate']}")
            print(f"Slot ID: {i['slot_id']}")
            print(f"Check In: {i['check_in']}")
            print(f"Check Out: {i['check_out']}")
            print(f"Status: {i['status']}")
            print("-" * 30)
def view_history_action():
    print("=== VIEW TRANSACTION HISTORY ===")
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    display_transaction_history(start, end)