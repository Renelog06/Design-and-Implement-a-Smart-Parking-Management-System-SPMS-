from datetime import datetime
import json
from data_handler import load_json

def load_transactions():
    transaction=load_json('data/transactions.json')
    return transaction

def search_by_date(start, end): 
    transactions = load_transactions() 
    matched = []
    for tr in transactions:
        ci = tr['check_in'][:10]
        co = tr['check_out'][:10] if tr['check_out'] else None

        # nếu chưa check out thì gán nhãn
        if tr['check_out'] is None:
            tr['check_out'] = "Still Parked"

        # chỉ append một lần nếu check-in hoặc check-out nằm trong khoảng
        if (start <= ci <= end) or (co and start <= co <= end):
            matched.append(tr)

    return matched

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
