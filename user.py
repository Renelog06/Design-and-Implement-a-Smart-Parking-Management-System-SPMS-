class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def get_username(self):
        return self.username

    def get_role(self):
        return self.role

    @staticmethod
    def admin_menu():
        print("1. Configure parking lot")
        print("2. Set pricing")
        print("3. Manage parking slots")
        print("4. View reports")
        print("5. Export reports")
        print("6. Delete old records")
        print("0. Exit")

    @staticmethod
    def attendant_menu():
        print("1. Vehicle check-in")
        print("2. Vehicle check-out")
        print("3. View available slots")
        print("4. View parked vehicles")
        print("5. Prevent duplicate check-in")
        print("6. Print receipt")
        print("0. Exit")

    @staticmethod
    def owner_menu():
        print("1. Find available slots")
        print("2. Register vehicle")
        print("3. View parking fee")
        print("4. Make payment")
        print("5. View parking history")
        print("0. Exit")

    def show_menu_by_role(self):
        role = self.get_role()
        if role == "admin":
            User.admin_menu()
        elif role == "attendant":
            User.attendant_menu()
        elif role == "owner":
            User.owner_menu()
        else:
            print(f"No menu for role '{role}'")
