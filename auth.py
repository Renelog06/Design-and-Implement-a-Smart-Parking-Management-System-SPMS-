from data_handler import load_json, save_json
from user import User

def register():
    users = load_json("data/users.json")
    user_name = input("Enter your name: ").strip()
    if any(i["username"] == user_name for i in users):
        print("❌ Username already exists.")
        return
    password = input("Enter your Password: ").strip()
    role = "owner"
    users.append({"username": user_name, "password": password, "role": role})
    save_json("data/users.json", users)
    print("✅ Registration successful")

def login():
    users = load_json("data/users.json")
    user_name = input("Username: ").strip()
    password = input("Password: ").strip()
    for i in users:
        if i["username"] == user_name and i["password"] == password:
            print(f"✅ Welcome back, {user_name} ({i['role']})!")
            return User(user_name, i["role"])
    print("❌ Invalid credentials.")
    return None
