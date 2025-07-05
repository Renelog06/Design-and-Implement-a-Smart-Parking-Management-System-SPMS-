from data_handler import load_json, save_json

VEHICLES_FILE = "data/vehicles.json"

def register_vehicle_if_not_exists(license_plate):
    """Tự động đăng ký xe nếu chưa có trong hệ thống."""
    vehicles = load_json(VEHICLES_FILE)
    if not isinstance(vehicles, list):
        vehicles = []

    # Kiểm tra xem xe đã tồn tại chưa
    if any(v.get('license_plate') == license_plate.upper() for v in vehicles):
        return # Đã tồn tại, không cần làm gì

    # Nếu chưa, thêm xe mới
    new_vehicle = {"license_plate": license_plate.upper()}
    vehicles.append(new_vehicle)
    save_json(VEHICLES_FILE, vehicles)
    print(f"ℹ️  Đã tự động đăng ký xe mới: {license_plate.upper()}")