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
            print("[MOCK] Setting pricing...")
        elif choice == "3":
            print("[MOCK] Managing parking slots...")
        elif choice == "4":
            view_reports()
        elif choice == "5":
            print("[MOCK] Exporting reports...")
        elif choice == "6":
            print("[MOCK] Deleting old records...")
        else:
            print("Invalid choice for admin.")

    elif role == "attendant":
        if choice == "1":
            print("[MOCK] Check in...")
        elif choice == "2":
            print("[MOCK] Check out...")
        elif choice == "3":
            print("[MOCK] Viewing available slots...")
        elif choice == "4":
            print("[MOCK] Viewing parked vehicles...")
        elif choice == "5":
            print("[MOCK] Preventing duplicate check-in...")
        elif choice == "6":
            print("[MOCK] Printing receipt...")
        else:
            print("Invalid choice for attendant.")

    elif role == "owner":
        if choice == "1":
            print("[MOCK] Finding available slots...")
        elif choice == "2":
            print("[MOCK] Registering vehicle...")
        elif choice == "3":
            print("[MOCK] Viewing parking fee...")
        elif choice == "4":
            print("[MOCK] Making payment...")
        elif choice == "5":
            print("[MOCK] Viewing parking history...")
        else:
            print("Invalid choice for owner.")

    else:
        print(f"No actions defined for role '{role}'.")

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
