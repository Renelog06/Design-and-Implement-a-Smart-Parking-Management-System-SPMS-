# main.py (phiên bản đã tích hợp)
from auth import login, register
from mockuser import show_menu_by_role
# <<< THAY ĐỔI Ở ĐÂY: Thêm các import mới
import slot
import transaction
from report import total_revenue, occupancy_rate, most_used_slots
from data_handler import load_json
# >>> KẾT THÚC THAY ĐỔI

# <<< THAY ĐỔI Ở ĐÂY: Tạo các hàm xử lý thật sự
def configure_lot_action():
    try:
        total = int(input("Nhập tổng số chỗ đỗ: "))
        slot.configure_parking_lot(total)
    except ValueError:
        print("❌ Vui lòng nhập một số nguyên.")

def check_in_vehicle_action():
    plate = input("Nhập biển số xe: ").strip()
    slot_id = input("Nhập vị trí đỗ (ví dụ: A001): ").strip().upper()
    transaction.check_in(plate, slot_id)

def check_out_vehicle_action():
    plate = input("Nhập biển số xe: ").strip()
    transaction.check_out(plate)

def view_available_slots_action():
    available = slot.get_available_slots()
    if not available:
        print("ℹ️ Hiện tại không còn chỗ đỗ nào trống.")
    else:
        print(f"--- Các chỗ đỗ còn trống ({len(available)}) ---")
        slot_ids = [s['slot_id'] for s in available]
        print(", ".join(slot_ids))
# >>> KẾT THÚC THAY ĐỔI

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
            # <<< THAY ĐỔI Ở ĐÂY: Gọi hàm thật
            configure_lot_action()
        elif choice == "2":
            view_reports()
    elif role == "attendant":
        if choice == "1":
            # <<< THAY ĐỔI Ở ĐÂY: Gọi hàm thật
            check_in_vehicle_action()
        elif choice == "2":
            # <<< THAY ĐỔI Ở ĐÂY: Gọi hàm thật
            check_out_vehicle_action()
    elif role == "owner":
        if choice == "1":
            # <<< THAY ĐỔI Ở ĐÂY: Gọi hàm thật
            view_available_slots_action()
        elif choice == "2":
            # <<< THAY ĐỔI Ở ĐÂY: Gọi hàm thật
            check_in_vehicle_action()
        elif choice == "3":
            # <<< THAY ĐỔI Ở ĐÂY: Gọi hàm thật
            check_out_vehicle_action()

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