from datetime import datetime
import uuid
from data_handler import load_json, save_json
from slot import get_slot_by_id, update_slot_status 
from vehicle import register_vehicle_if_not_exists

TRANSACTIONS_FILE = "data/transactions.json"

def find_active_transaction(license_plate):
    """Tìm giao dịch đang hoạt động (chưa check-out) của xe."""
    transactions = load_json(TRANSACTIONS_FILE)
    if not isinstance(transactions, list): return None
    
    for tx in transactions:
        if tx.get('license_plate') == license_plate.upper() and tx.get('status') == 'parked':
            return tx
    return None

def check_in(license_plate, slot_id):
    """Xử lý check-in cho xe."""
    # Tự động đăng ký xe nếu chưa có
    register_vehicle_if_not_exists(license_plate)

    # Kiểm tra các điều kiện
    if find_active_transaction(license_plate):
        print(f"❌ Lỗi: Xe {license_plate.upper()} đã ở trong bãi.")
        return

    slot = get_slot_by_id(slot_id)
    if not slot:
        print(f"❌ Lỗi: Chỗ đỗ '{slot_id}' không tồn tại.")
        return
    if slot.get('is_occupied'):
        print(f"❌ Lỗi: Chỗ đỗ '{slot_id}' đã có xe.")
        return
    
    # Tạo giao dịch mới
    transactions = load_json(TRANSACTIONS_FILE)
    if not isinstance(transactions, list): transactions = []
    
    new_transaction = {
        "transaction_id": str(uuid.uuid4().hex[:8]),
        "license_plate": license_plate.upper(),
        "slot_id": slot_id,
        "check_in": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "check_out": None,
        "fee": 0,
        "status": "parked"
    }
    transactions.append(new_transaction)
    save_json(TRANSACTIONS_FILE, transactions)
    
    # Cập nhật trạng thái chỗ đỗ
    update_slot_status(slot_id, True)
    print(f"✅ Check-in thành công cho xe {license_plate.upper()} tại vị trí {slot_id}.")

def check_out(license_plate):
    """Xử lý check-out cho xe."""
    active_tx = find_active_transaction(license_plate)
    if not active_tx:
        print(f"❌ Lỗi: Xe {license_plate.upper()} không có trong bãi hoặc đã check-out.")
        return

    # Tính phí (ví dụ: 10,000 VND/giờ)
    check_in_time = datetime.strptime(active_tx["check_in"], "%Y-%m-%d %H:%M:%S")
    hours = (datetime.now() - check_in_time).total_seconds() / 3600
    fee = max(1, round(hours)) * 10000 # Ít nhất 1 giờ

    # Cập nhật giao dịch
    transactions = load_json(TRANSACTIONS_FILE)
    for tx in transactions:
        if tx.get("transaction_id") == active_tx.get("transaction_id"):
            tx["status"] = "completed"
            tx["check_out"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tx["fee"] = fee
            break
    save_json(TRANSACTIONS_FILE, transactions)
    
    # Cập nhật trạng thái chỗ đỗ
    update_slot_status(active_tx["slot_id"], False)
    print(f"✅ Check-out thành công cho xe {license_plate.upper()}.")
    print(f"   Tổng phí: {fee:,} VND")