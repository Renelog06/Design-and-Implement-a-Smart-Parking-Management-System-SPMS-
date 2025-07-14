from datetime import datetime
import uuid
from data_handler import load_json, save_json
from slot import get_slot_by_id, update_slot_status 
from vehicle import register_vehicle_if_not_exists

TRANSACTIONS_FILE = "data/transactions.json"

def find_active_transaction(license_plate):
    """Tìm giao dịch đang hoạt động (chưa check-out) của xe."""
    transactions = load_json(TRANSACTIONS_FILE)
    if not isinstance(transactions, list):
        return None
    
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
    if not isinstance(transactions, list):
        transactions = []
    
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

    # Tính thời gian đỗ
    check_in_time = datetime.strptime(active_tx["check_in"], "%Y-%m-%d %H:%M:%S")
    hours = (datetime.now() - check_in_time).total_seconds() / 3600
    actual_hours = max(1, hours)  # ít nhất là 1 giờ

    # Cấu hình phí
    FEE_PER_HOUR = 2000
    ONE_DAY_HOURS = 24
    OVER_28_DAYS_HOURS = 28 * 24  # 672 giờ

    # Tính phí gốc
    fee = actual_hours * FEE_PER_HOUR

    # Điều chỉnh theo thời gian đỗ
    if ONE_DAY_HOURS <= actual_hours <= OVER_28_DAYS_HOURS:
        fee *= 2  # Tăng gấp đôi nếu đỗ từ 1 đến 28 ngày
    elif actual_hours > OVER_28_DAYS_HOURS:
        fee *= 0.8  # Giảm 20% nếu đỗ trên 28 ngày
    else:
        fee *= 0.9  # Giảm 10% nếu dưới 1 ngày

    fee = int(round(fee))

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

    # In thông tin cho người dùng
    print(f"✅ Check-out thành công cho xe {license_plate.upper()}.")
    print(f"   Thời gian đỗ: {actual_hours:.2f} giờ")
    print(f"   Tổng phí: {fee:,} VND")
