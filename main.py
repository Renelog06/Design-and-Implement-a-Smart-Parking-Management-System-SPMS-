from auth import login, register
from user import User

def check_in_vehicle():
    print("[MOCK] Check-in vehicle...")

def check_out_vehicle():
    print("[MOCK] Check-out vehicle...")

def view_revenue_reports():
    print("[MOCK] Viewing revenue reports...")

def handle_action(user, choice):
    role = user.get_role()
    if role == "admin":
        if choice == "1":
            print("[MOCK] Configuring parking lot...")
        elif choice == "2":
            view_revenue_reports()
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
    User.load_users()  # Load dữ liệu user từ file data.json
    while True:
        print("1. Login\n2. Register\n0. Exit")
        opt = input("Choose: ")
        if opt == "1":
            user = login()
            if user:
                while True:
                    role = user.get_role()
                    if role == "admin":
                        User.admin_menu()
                    elif role == "attendant":
                        User.attendant_menu()
                    elif role == "owner":
                        User.owner_menu()
                    else:
                        print("Unknown role!")
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
