from data_handler import load_json, save_json

def config_pricing_setting():
    """Cấu hình mức phí đỗ xe"""
    # Tải cấu hình hiện tại
    current_config = load_json("data/pricing.json")
    
    # Kiểm tra và thiết lập giá trị mặc định nếu cần
    if not current_config or not isinstance(current_config, dict):
        current_config = {
            "base_hourly_rate": 2000,
            "daily_discount": 0.1,
            "monthly_discount": 0.2
        }
    
    # Đảm bảo có đầy đủ các key cần thiết
    current_config.setdefault("base_hourly_rate", 2000)
    current_config.setdefault("daily_discount", 0.1)
    current_config.setdefault("monthly_discount", 0.2)
    
    print("\n--- CẤU HÌNH MỨC PHÍ ---")
    print(f"Giá hiện tại: {current_config['base_hourly_rate']} VND/giờ")
    print(f"Giảm giá theo ngày: {current_config['daily_discount'] * 100}%")
    print(f"Giảm giá theo tháng: {current_config['monthly_discount'] * 100}%")
    print("(Nhấn Enter để giữ nguyên giá trị hiện tại)\n")
    
    try:
        # Nhập giá cơ bản
        new_rate = input(f"Nhập giá mới (VND/giờ) [{current_config['base_hourly_rate']}]: ").strip()
        if new_rate:
            current_config['base_hourly_rate'] = int(new_rate)
            print(f"✓ Đã cập nhật giá: {new_rate} VND/giờ")
        
        # Nhập giảm giá theo ngày
        new_daily = input(f"Nhập % giảm giá theo ngày (0-100) [{current_config['daily_discount'] * 100}]: ").strip()
        if new_daily:
            current_config['daily_discount'] = float(new_daily) / 100
            print(f"✓ Đã cập nhật giảm giá ngày: {new_daily}%")
        
        # Nhập giảm giá theo tháng
        new_monthly = input(f"Nhập % giảm giá theo tháng (0-100) [{current_config['monthly_discount'] * 100}]: ").strip()
        if new_monthly:
            current_config['monthly_discount'] = float(new_monthly) / 100
            print(f"✓ Đã cập nhật giảm giá tháng: {new_monthly}%")
        
        # Lưu cấu hình
        print("\nĐang lưu cấu hình...")
        save_json("data/pricing.json", current_config)
        print(f"Đã lưu: {current_config}")
        print("✅ Cấu hình mức phí đã được cập nhật thành công!")
        
    except ValueError:
        print("❌ Vui lòng nhập số hợp lệ.")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

def display_pricing_info():
    """Hiển thị thông tin mức phí hiện tại"""
    pricing_data = load_json("data/pricing.json")
    
    if not pricing_data:
        print("ℹ️ Chưa có cấu hình mức phí.")
        return
    
    hourly_rate = pricing_data.get("base_hourly_rate", 2000)
    daily_discount = pricing_data.get("daily_discount", 0.1)
    monthly_discount = pricing_data.get("monthly_discount", 0.2)
    
    print("\n--- THÔNG TIN MỨC PHÍ ---")
    print(f"💰 Giá cơ bản: {hourly_rate:,} VND/giờ")
    print(f"🎯 Giảm giá theo ngày (≥24h): {daily_discount * 100}%")
    print(f"🎁 Giảm giá theo tháng (≥720h): {monthly_discount * 100}%")
    
    # Ví dụ tính phí
    print("\n--- VÍ DỤ TÍNH PHÍ ---")
    examples = [
        ("2 giờ", 2, 0),
        ("8 giờ", 8, 0),
        ("1 ngày (24 giờ)", 24, daily_discount),
        ("1 tuần (168 giờ)", 168, daily_discount),
        ("1 tháng (720 giờ)", 720, monthly_discount)
    ]
    
    for desc, hours, discount in examples:
        base_fee = hours * hourly_rate
        final_fee = int(base_fee * (1 - discount))
        saved_amount = int(base_fee - final_fee)
        
        if discount > 0:
            print(f"• {desc}: {final_fee:,} VND (giảm {discount * 100}% - tiết kiệm {saved_amount:,} VND)")
        else:
            print(f"• {desc}: {final_fee:,} VND")