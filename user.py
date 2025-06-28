import json

class User:
    users = {}

    @classmethod
    def load_users(cls, filename="data.json"):
        with open(filename, "r", encoding="utf-8") as f:
            cls.users = json.load(f)

    def __init__(self, username, role):
        self.username = username
        self.role = role

    @classmethod
    def login(cls, username, password):
        if username in cls.users and cls.users[username]["password"] == password:
            return User(username, cls.users[username]["role"])
        else:
            return None

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

    def get_role(self):
        return self.role


