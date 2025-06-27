class User:
    users = {
        "admin": {
            "password": "admin123",
            "role": "admin"
        },
        "Parking Attendant": {
            "password": "attendant123",
            "role": "attendant"
        },
        "Vehicle Owner": {
            "password": "owner123",
            "role": "owner"
        },
    }

    def __init__(self, username, role):
        self.username = username
        self.role = role

    @classmethod
    def login(cls, username, password):
        if username in cls.users and cls.users[username]["password"] == password:
            return User(username, cls.users[username]["role"])
        else:
            return None
    def admin_menu():
        print("1. Manage slots")
        print("2. Set hourly rates")
        print("3. Export revenue reports")
    def attendant_menu():
        print("1. Check-in vehicles")
        print("2. Check-out vehicles")
        print("3. Update slots")
    def owner_menu():
        print("1. View available slots")
        print("2. Pay parking fees")



