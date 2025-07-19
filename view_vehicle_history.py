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
            i['check_out'] = "Vẫn đang đậu"
            day.append(i)
    return day

def display_transaction_history(start, end):
    transaction= search_by_date(start, end)
    if transaction==[]:
        print("Không có giao dịch nào trong khoảng thời gian này.")
    else:
        print(f"=== CÁC GIAO DỊCH TỪ {start} ĐẾN {end} ===")
        for i in transaction:
            print(f"Biển số: {i['license_plate']}")
            print(f"Vị trí: {i['slot_id']}")
            print(f"Ngày vào: {i['check_in']}")
            print(f"Ngày ra: {i['check_out']}")
            print(f"Trạng thái: {i['status']}")
            print("-" * 30)
def view_history_action():
    print("=== XEM LỊCH SỬ GIAO DỊCH ===")
    start = input("Nhập ngày bắt đầu (YYYY-MM-DD): ")
    end = input("Nhập ngày kết thúc (YYYY-MM-DD): ")
    display_transaction_history(start, end)