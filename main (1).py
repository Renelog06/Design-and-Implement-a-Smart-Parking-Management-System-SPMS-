from auth import login, register
from user import show_menu_by_role
from slot import get_slot_by_id, get_available_slots, configure_parking_lot
from report import total_revenue, occupancy_rate, most_used_slots
from data_handler import load_json
from addanddelete import add_slot_action, delete_slot_action 
from check_in_out import check_in_vehicle_action, check_out_vehicle_action
from search_vehicles import search_vehicle
from fee import pricing_setting, display_current_pricing
import transaction

def configure_lot_action():
    try:
        total = int(input("Nhập tổng số chỗ đỗ: "))
        configure_parking_lot(total)
    except ValueError:
        print("❌ Vui lòng nhập một số nguyên.")

def view_available_slots_action():
    available = get_available_slots()
    if not available:
        print("ℹ️ Hiện tại không còn chỗ đỗ nào trống.")
    else:
        print(f"--- Các chỗ đỗ còn trống ({len(available)}) ---")
        slot_ids = [s['slot_id'] for s in available]
        print(", ".join(slot_ids))

def view_reports():
    transactions = load_json("data/transactions.json")
    if not isinstance(transactions, list) or not transactions:
        print("ℹ️ Chưa có dữ liệu giao dịch để tạo báo cáo.")
        return

    print("\n--- BÁO CÁO ---")
    print("Doanh thu hôm nay:", total_revenue(transactions, "daily"), "VND")
    print("Doanh thu tuần này:", total_revenue(transactions, "weekly"), "VND")
    print("Doanh thu tháng này:", total_revenue(transactions, "monthly"), "VND")
    
    # Giả sử bãi xe có 50 chỗ nếu chưa cấu hình
    total_slots = len(load_json("data/slots.json") or []) or 50 
    print("Tỷ lệ sử dụng chỗ đỗ:", occupancy_rate(transactions, total_slots), "%")
    print("Các vị trí được sử dụng nhiều nhất:", most_used_slots(transactions))
    print("------------")

def search_currently_vechicles():
    license_plate = input("Enter your license plate: ")
    search_vehicle(license_plate)
def display_pricing_info():
    pricing_info = load_json("data/pricing.json")
    if not pricing_info:
        print("ℹ️ Chưa có cấu hình mức phí.")
        return

def config_pricing_setting():
    pricing_setting = load_json("data/pricing.json")
    if not pricing_setting:
        print("ℹ️ Chưa có cấu hình mức phí.")
        return {"base_hourly_rate": 2000}

def handle_action(user, choice):
    role = user.get_role()
    if role == "admin":
        if choice == "1":
            configure_lot_action()
        elif choice == "2":
            view_reports()
        elif choice == "3":          
            add_slot_action()
        elif choice == "4":          
            delete_slot_action()
        elif choice == "5":          
            pricing_setting()
        elif choice == "6":          
            display_current_pricing()
    elif role == "attendant":
        if choice == "1":
            view_available_slots_action()
        elif choice == "2":
            search_currently_vechicles()
        elif choice == "3":
            check_in_vehicle_action()
        elif choice == "4":
            check_out_vehicle_action()
        elif choice == "5":          
            display_current_pricing()
    elif role == "owner":
        if choice == "1":
            view_available_slots_action()
        elif choice == "2":
            check_in_vehicle_action()
        elif choice == "3":
            print("check estimated parking fee")
        elif choice == "4":
            get_slot_by_id("data/slots.json")
        elif choice == "5":          
            pricing_setting()
        elif choice == "6":          
            display_current_pricing()

def main():
    while True:
        print("\n1. Login\n2. Register\n0. Exit")
        opt = input("Choose: ")
        if opt == "1":
            user = login()
            if user:
                while True:
                    print("-" * 20)
                    show_menu_by_role(user)
                    choice = input("Your choice: ")
                    if choice == "0":
                        break
                    handle_action(user, choice)
        elif opt == "2":
            register()
        elif opt == "0":
            print("👋 Tạm biệt!")
            break

if __name__ == "__main__":
    main()
