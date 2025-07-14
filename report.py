from datetime import datetime
from data_handler import load_json

def total_revenue(transactions, period = "daily"):
    total = 0
    for transaction in transactions:
        if transaction["status"] != "completed":
            continue
        else:
            check_out = datetime.strptime(transaction["check_out"], "%Y-%m-%d %H:%M:%S")
            if period == "daily" and check_out.date() == datetime.now().date() and check_out.year == datetime.now().year:
                total += transaction["fee"]
            elif period == "weekly" and check_out.isocalendar()[1] == datetime.now().isocalendar()[1] and check_out.year == datetime.now().year:
                total += transaction["fee"]
            elif period == "monthly" and check_out.month == datetime.now().month and check_out.year == datetime.now().year:
                total += transaction["fee"]
    return total

def occupancy_rate(transactions, total_slots):
    used_slots = []
    if not transactions:
        return 0
    else:
        for transaction in transactions:
            if transaction["status"] == "completed":
                used_slots.append(transaction["slot_id"])
        rate = (len(used_slots)/total_slots)*100
        return  round(rate, 2)

def most_used_slots(transactions):
    count={}
    for transaction in transactions:
        if transaction["status"] == "completed":
            slot = transaction["slot_id"]
            count[slot] = count.get(slot, 0) + 1
    most_slots = []
    max_count = 0
    for slot, c in count.items():
        if c > max_count:
            max_count = c
    for slot, c in count.items():
        if c == max_count:
            most_slots.append(slot)
    return most_slots