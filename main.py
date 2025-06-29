from auth import login, register
from user import User
from report import total_revenue, occupancy_rate, most_used_slots
from data_handler import load_json

def check_in_vehicle():
    print("[MOCK] Check-in vehicle...")

def check_out_vehicle():
    print("[MOCK] Check-out vehicle...")

def view_reports():
    transactions = load_json("data/transactions.json")
    print("total revenue today:", total_revenue(transactions, "daily"), "VND")
    print("Total revenue of this month:", total_revenue(transactions, "monthly"), "VND")
    print("Total revenue of this week::", total_revenue(transactions, "weekly"), "VND")
    print("The rate of parking space usage:", occupancy_rate(transactions, total_slots=10), "%")
    print("The most used slot:", most_used_slots(transactions))

def handle_action(user, choice):
    role = user.get_role()
    if role == "admin":
        if choice == "1":
            print("[MOCK] Configuring parking lot...")
        elif choice == "2":
            view_reports()
    elif role == "attendant":
        if choice == "1":
            check_in_vehicle()
        elif choice == "2":
            check_out_vehicle()
    elif role == "owner":
        if choice == "1":
            print("[MOCK] Viewing available slots...")
        elif choice == "2":
            check_in_vehicle()
        elif choice == "3":
            check_out_vehicle()

def main():
    while True:
        print("1. Login\n2. Register\n0. Exit")
        opt = input("Choose: ")
        if opt == "1":
            user = login()
            if user:
                while True:
                    user.show_menu_by_role()
                    choice = input("Your choice: ")
                    if choice == "0":
                        break
                    handle_action(user, choice)
        elif opt == "2":
            register()
        elif opt == "0":
            break

if __name__ == "__main__":
    main()
