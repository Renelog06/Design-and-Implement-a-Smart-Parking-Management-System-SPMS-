import json
from mockuser import User

User_file = "data/users.json"

def load_user():
    try:
        with open(User_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def save_user(users):
    with open(User_file, "w") as f:
        return json.dump(users, f, indent = 4)

def register():
    users = load_user()
    user_name = input("Enter your name: ").strip()
    if any(i["username"] == user_name for i in users):
        print("❌ Username already exists.")
        return
    password = input("Enter your Password: ").strip()
    role = "owner"
    users.append({"username": user_name, "password": password, "role": role})
    save_user(users)
    print("✅ Registration successful")

def login():
    users = load_user()
    user_name = input("Username: ").strip()
    password = input("Password: ").strip()
    for i in users:
        if i["username"] == user_name and i["password"] == password:
            print(f"✅ Welcome back, {user_name} ({i['role']})!")
            return User(user_name, i["role"])
    print("❌ Invalid credentials.")
    return None