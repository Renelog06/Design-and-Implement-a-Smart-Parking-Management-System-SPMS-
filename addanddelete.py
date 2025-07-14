from data_handler import load_json, save_json
from slot import SLOTS_FILE, get_available_slots
from transaction import TRANSACTIONS_FILE

def add_slot(slot_id):
    """Thêm một chỗ đỗ mới vào danh sách."""
    slots = load_json(SLOTS_FILE)
    if not isinstance(slots, list):
        slots = []

    if any(s.get('slot_id') == slot_id.upper() for s in slots):
        print(f"❌ Lỗi: Chỗ đỗ '{slot_id.upper()}' đã tồn tại.")
        return

    new_slot = {"slot_id": slot_id.upper(), "is_occupied": False}
    slots.append(new_slot)
    save_json(SLOTS_FILE, slots)
    print(f"✅ Đã thêm thành công chỗ đỗ mới: {slot_id.upper()}")



def delete_slot(slot_id_to_delete):
    """Xóa một chỗ đỗ. Nếu có xe, hỏi người dùng xác nhận trước khi di dời."""
    slot_id_to_delete = slot_id_to_delete.upper()
    slots = load_json(SLOTS_FILE)
    
    slot_to_delete = next((s for s in slots if s.get('slot_id') == slot_id_to_delete), None)
    
    if not slot_to_delete:
        print(f"❌ Lỗi: Không tìm thấy chỗ đỗ với ID '{slot_id_to_delete}'.")
        return
    if slot_to_delete.get('is_occupied'):
        

        prompt = (f"⚠️ Chỗ đỗ '{slot_id_to_delete}' đang có xe. "
                f"Bạn có muốn di dời xe này sang chỗ trống khác không? (y/n): ")
        choice = input(prompt).lower().strip()

        if choice != 'y':
            print("ℹ️ Thao tác xóa đã được hủy bởi người dùng.")
            return

        print(f"ℹ️ Đang tìm chỗ trống để di dời...")
        
        available_slots = get_available_slots()
        available_slots = [s for s in available_slots if s.get('slot_id') != slot_id_to_delete]

        if not available_slots:
            print(f"❌ Lỗi: Không còn chỗ trống nào để di dời xe. Thao tác xóa đã bị hủy.")
            return
        
        new_slot = available_slots[0]
        new_slot_id = new_slot['slot_id']
        
        transactions = load_json(TRANSACTIONS_FILE)
        vehicle_license_plate = ""
        for tx in transactions:
            if tx.get('slot_id') == slot_id_to_delete and tx.get('status') == 'parked':
                vehicle_license_plate = tx.get('license_plate')
                tx['slot_id'] = new_slot_id
                break
        
        if vehicle_license_plate:
            for s in slots:
                if s.get('slot_id') == new_slot_id:
                    s['is_occupied'] = True
                    break
            
            save_json(TRANSACTIONS_FILE, transactions)
            print(f"✅ Đã tự động di dời xe {vehicle_license_plate} từ '{slot_id_to_delete}' đến '{new_slot_id}'.")
        else:
            print(f"⚠️ Cảnh báo: Không tìm thấy giao dịch đang hoạt động cho chỗ '{slot_id_to_delete}'. Bỏ qua bước di dời.")

    # Xóa chỗ đỗ cũ khỏi danh sách
    updated_slots = [s for s in slots if s.get('slot_id') != slot_id_to_delete]
    save_json(SLOTS_FILE, updated_slots)
    print(f"✅ Đã xóa thành công chỗ đỗ: {slot_id_to_delete}")


def add_slot_action():
    """Hỏi người dùng và gọi hàm add_slot."""
    slot_id = input("Nhập ID chỗ đỗ cần thêm (ví dụ: A100): ").strip().upper()
    if not slot_id:
        print("❌ ID chỗ đỗ không được để trống.")
        return
    add_slot(slot_id) # Gọi hàm logic 

def delete_slot_action():
    """Hỏi người dùng và gọi hàm delete_slot."""
    slot_id = input("Nhập ID chỗ đỗ cần xóa: ").strip().upper()
    if not slot_id:
        print("❌ ID chỗ đỗ không được để trống.")
        return
    delete_slot(slot_id) # Gọi hàm logic 