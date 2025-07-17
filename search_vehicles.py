from data_handler import load_json

def search_vehicle(license_plate):
    transactions = load_json('data/transactions.json')
    found = False
    for vehicle in transactions:
        if license_plate.upper() == vehicle['license_plate'] and vehicle['status'] == "parked":
            print("------Found vehicle---------")
            print(f"License Plate: {vehicle['license_plate']}")
            print(f"Transaction ID: {vehicle['transaction_id']}")
            print(f"Slot ID: {vehicle['slot_id']}")
            print(f"Check in time: {vehicle['check_in']}")
            found = True
            break
    if found == False:
        print("------Your vehicle cannot found!---------")

