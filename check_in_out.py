import transaction

def check_in_vehicle_action():
    plate = input("Nhập biển số xe: ").strip()
    slot_id = input("Nhập vị trí đỗ (ví dụ: A001): ").strip().upper()
    transaction.check_in(plate, slot_id)

def check_out_vehicle_action():
    plate = input("Nhập biển số xe: ").strip()
    transaction.check_out(plate)