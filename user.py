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

u = input("Enter username: ")
p = input("Enter password: ")

data = User.login(u, p)
if data:
    print(f"Login successful! Welcome {data.username} ")
else:
    print("Login failed! Please check your username and password.")
