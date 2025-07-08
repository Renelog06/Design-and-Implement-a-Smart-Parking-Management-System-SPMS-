class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def get_username(self):
        return self.username

    def get_role(self):
        return self.role

def admin_menu():
    print("1. Configure parking lot")
    print("2. View revenue reports")
    print("3. Add parking slot")
    print("4. Delete parking slot")
    print("0. Logout")

def attendant_menu():
    print("1. Check-in vehicle")
    print("2. Check-out vehicle")
    print("0. Logout")

def owner_menu():
    print("1. View available slots")
    print("2. Check-in vehicle")
    print("3. Check-out vehicle")
    print("0. Logout")

def show_menu_by_role(user):
    role = user.get_role()
    if role == "admin":
        admin_menu()
    elif role == "attendant":
        attendant_menu()
    elif role == "owner":
        owner_menu()
