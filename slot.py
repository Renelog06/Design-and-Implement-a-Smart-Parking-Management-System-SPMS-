from data_handler import load_json, save_json

SLOTS_FILE = "data/slots.json"

def configure_parking_lot(total_slots):
    """Tạo hoặc ghi đè file cấu hình các chỗ đỗ xe."""
    if total_slots <= 0:
        print("❌ Tổng số chỗ đỗ phải là số dương.")
        return
    
    slots = [{"slot_id": f"A{i:03}", "is_occupied": False} for i in range(1, total_slots + 1)]
    save_json(SLOTS_FILE, slots)
    print(f"✅ Đã cấu hình thành công {total_slots} chỗ đỗ.")

def get_available_slots():
    """Lấy danh sách các chỗ đỗ còn trống."""
    slots = load_json(SLOTS_FILE)
    if not isinstance(slots, list): return []
    return [s for s in slots if not s.get('is_occupied')]

def get_slot_by_id(slot_id):
    """Tìm một chỗ đỗ bằng ID."""
    slots = load_json(SLOTS_FILE)
    if not isinstance(slots, list): return None
    for s in slots:
        if s.get('slot_id') == slot_id:
            return s
    return None

def update_slot_status(slot_id, is_occupied):
    """Cập nhật trạng thái của một chỗ đỗ."""
    slots = load_json(SLOTS_FILE)
    if not isinstance(slots, list): 
        print(f"❌ Lỗi: Dữ liệu slot không hợp lệ.")
        return False

    slot_found = False
    for s in slots:
        if s.get('slot_id') == slot_id:
            s['is_occupied'] = is_occupied
            slot_found = True
            break
    
    if slot_found:
        save_json(SLOTS_FILE, slots)
        return True
    
    print(f"❌ Lỗi: Không tìm thấy chỗ đỗ với ID '{slot_id}'.")
    return False