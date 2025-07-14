def check_out(license_plate):
    """Xử lý check-out cho xe."""
    active_tx = find_active_transaction(license_plate)
    if not active_tx:
        print(f"❌ Lỗi: Xe {license_plate.upper()} không có trong bãi hoặc đã check-out.")
        return

    # Tính phí theo mức linh hoạt
    check_in_time = datetime.strptime(active_tx["check_in"], "%Y-%m-%d %H:%M:%S")
    hours = (datetime.now() - check_in_time).total_seconds() / 3600
    rounded_hours = max(1, round(hours))

    # Cấu hình phí
    FEE_PER_HOUR = 2000
    ONE_DAY = 24
    OVER_28_DAYS = 28 * 24  # 672 giờ

    # Tính phí cơ bản
    fee = rounded_hours * FEE_PER_HOUR

    # Điều chỉnh phí
    if rounded_hours == ONE_DAY:
        fee *= 2  # Tăng gấp đôi nếu đỗ đúng 1 ngày
    elif rounded_hours > OVER_28_DAYS:
        fee *= 0.8  # Giảm 20% nếu đỗ trên 28 ngày
    else:
        fee *= 0.9  # Giảm 10% nếu không vượt 28 ngày

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
    print(f"✅ Check-out thành công cho xe {license_plate.upper()}.")
    print(f"   Tổng phí: {fee:,} VND")
