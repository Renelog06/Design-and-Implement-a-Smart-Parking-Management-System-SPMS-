from datetime import datetime
import uuid
from data_handler import load_json, save_json
from slot import get_slot_by_id, update_slot_status 
from vehicle import register_vehicle_if_not_exists

TRANSACTIONS_FILE = "data/transactions.json"
PRICING_FILE = "data/pricing.json"

def _get_pricing_rules():
    """Tải các quy tắc tính phí từ file config, cung cấp giá trị mặc định nếu file không tồn tại."""
    pricing_config = load_json(PRICING_FILE)
    if not isinstance(pricing_config, dict):
        return {"base_hourly_rate": 10000, "daily_discount": 0.0, "monthly_discount": 0.0}
    pricing_config.setdefault("base_hourly_rate", 10000)
    pricing_config.setdefault("daily_discount", 0.0)
    pricing_config.setdefault("monthly_discount", 0.0)
    return pricing_config

def find_active_transaction(license_plate):
    transactions = load_json(TRANSACTIONS_FILE)
    if not isinstance(transactions, list): return None
    for tx in transactions:
        if tx.get('license_plate') == license_plate.upper() and tx.get('status') == 'parked':
            return tx
    return None

def check_in(license_plate, slot_id):
    register_vehicle_if_not_exists(license_plate)
    if find_active_transaction(license_plate):
        print(f"❌ Lỗi: Xe {license_plate.upper()} đã ở trong bãi.")
        return
    slot = get_slot_by_id(slot_id)
    if not slot or slot.get('is_occupied'):
        print(f"❌ Lỗi: Chỗ đỗ '{slot_id}' không hợp lệ hoặc đã có xe.")
        return
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
    update_slot_status(slot_id, True)
    print(f"✅ Check-in thành công cho xe {license_plate.upper()} tại vị trí {slot_id}.")

def check_out(license_plate):
    active_tx = find_active_transaction(license_plate)
    if not active_tx:
        print(f"❌ Lỗi: Xe {license_plate.upper()} không có trong bãi hoặc đã check-out.")
        return

    # <<< FIX: Tính phí dựa trên quy tắc từ fee.py >>>
    check_in_time = datetime.strptime(active_tx["check_in"], "%Y-%m-%d %H:%M:%S")
    hours_parked = (datetime.now() - check_in_time).total_seconds() / 3600
    rules = _get_pricing_rules()
    base_rate = rules["base_hourly_rate"]
    base_fee = max(1, round(hours_parked)) * base_rate
    discount_rate = 0
    if hours_parked >= 720: # 30 ngày
        discount_rate = rules["monthly_discount"]
    elif hours_parked >= 24: # 1 ngày
        discount_rate = rules["daily_discount"]
    final_fee = int(base_fee * (1 - discount_rate))
    # <<< END FIX >>>

    transactions = load_json(TRANSACTIONS_FILE)
    for tx in transactions:
        if tx.get("transaction_id") == active_tx.get("transaction_id"):
            tx["status"] = "completed"
            tx["check_out"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tx["fee"] = final_fee
            break
    save_json(TRANSACTIONS_FILE, transactions)
    update_slot_status(active_tx["slot_id"], False)
    print(f"✅ Check-out thành công cho xe {license_plate.upper()}.")
    print(f"   Tổng phí: {final_fee:,} VND")
