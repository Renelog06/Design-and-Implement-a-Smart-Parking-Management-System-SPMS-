
from auth import login, register
from user import show_menu_by_role
from slot import get_slot_by_id, get_available_slots, configure_parking_lot
from report import total_revenue, occupancy_rate, most_used_slots
from data_handler import load_json, save_json 
from addanddelete import add_slot_action, delete_slot_action 
from check_in_out import check_in_vehicle_action, check_out_vehicle_action
import transaction

# <<< PHẦN CẬP NHẬT NẰM Ở HÀM NÀY >>>
def configure_lot_action():
    """Hỏi xác nhận trước khi xóa dữ liệu cũ và cấu hình lại bãi xe."""
    print("\n⚠️ CẢNH BÁO: Hành động này sẽ XÓA SẠCH toàn bộ dữ liệu giao dịch (transactions) và xe cộ (vehicles).")
    print("Dữ liệu người dùng (users) sẽ không bị ảnh hưởng.")
    confirm = input("Bạn có chắc chắn muốn tiếp tục không? (y/n): ").lower().strip()
    
    if confirm != 'y':
        print("ℹ️ Thao tác đã được hủy.")
        return

    print("ℹ️ Đang xóa dữ liệu cũ...")
    save_json("data/transactions.json", [])
    save_json("data/vehicles.json", [])
    print("✅ Đã xóa dữ liệu giao dịch và xe cộ thành công.")
    
    try:
        total = int(input("Nhập tổng số chỗ đỗ mới: "))
        configure_parking_lot(total)
    except ValueError:
        print("❌ Vui lòng nhập một số nguyên.")
# <<< KẾT THÚC PHẦN CẬP NHẬT >>>


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
    elif role == "attendant":
        if choice == "1":
            view_available_slots_action()
        elif choice == "2":
            check_in_vehicle_action()
        elif choice == "3":
            check_out_vehicle_action()
    elif role == "owner":
        if choice == "1":
            view_available_slots_action()
        elif choice == "2":
            check_in_vehicle_action()
        elif choice == "3":
            print("check estimated parking fee")
        elif choice == "4":
            slot_id_input = input("Nhập ID chỗ đỗ cần tìm: ").strip().upper()
            if slot_id_input:
                slot_info = get_slot_by_id(slot_id_input)
                if slot_info:
                    print(f"--> Thông tin: {slot_info}")
                else:
                    print(f"--> Không tìm thấy chỗ đỗ {slot_id_input}")
            else:
                print("ID không được để trống.")


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
=======
from auth import login, register
from user import show_menu_by_role
from slot import get_slot_by_id, get_available_slots, configure_parking_lot
from report import total_revenue, occupancy_rate, most_used_slots
from data_handler import load_json
from addanddelete import add_slot_action, delete_slot_action 
from check_in_out import check_in_vehicle_action, check_out_vehicle_action
from search_vehicles import search_vehicle
from transaction import get_slot_by_id
from fee import config_pricing_setting, display_pricing_info

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
            display_pricing_info()
        elif choice == "6":          
            config_pricing_setting()
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
            display_pricing_info()
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
            display_pricing_info()
        elif choice == "6":          
            config_pricing_setting()

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

