class PricingSystem:
    def __init__(self):
        self.hourly_rate = 2000  # Giá mặc định 2000 VND/giờ
        self.daily_discount = 0.1  # Giảm 10% khi đủ 1 ngày
        self.monthly_discount = 0.2  # Giảm 20% khi trên 1 tháng
        
    def pricing_setting(self, new_hourly_rate=None, new_daily_discount=None, new_monthly_discount=None):
        """
        Cài đặt giá và mức giảm giá
        
        Args:
            new_hourly_rate: Giá mới theo giờ (VND)
            new_daily_discount: Mức giảm giá theo ngày (0.1 = 10%)
            new_monthly_discount: Mức giảm giá theo tháng (0.2 = 20%)
        """
        if new_hourly_rate is not None:
            self.hourly_rate = new_hourly_rate
            print(f"Đã cập nhật giá theo giờ: {self.hourly_rate:,} VND/giờ")
            
        if new_daily_discount is not None:
            self.daily_discount = new_daily_discount
            print(f"Đã cập nhật giảm giá theo ngày: {self.daily_discount * 100}%")
            
        if new_monthly_discount is not None:
            self.monthly_discount = new_monthly_discount
            print(f"Đã cập nhật giảm giá theo tháng: {self.monthly_discount * 100}%")
    
    def pricing_info(self, hours):
        """
        Tính toán thông tin giá dựa trên số giờ sử dụng
        
        Args:
            hours: Số giờ sử dụng dịch vụ
            
        Returns:
            dict: Thông tin chi tiết về giá
        """
        if hours <= 0:
            return {"error": "Số giờ phải lớn hơn 0"}
        
        # Tính giá gốc
        base_price = hours * self.hourly_rate
        
        # Xác định mức giảm giá
        discount_rate = 0
        discount_type = "Không giảm giá"
        
        if hours >= 24 * 30:  # Trên 1 tháng (720 giờ)
            discount_rate = self.monthly_discount
            discount_type = "Giảm giá theo tháng"
        elif hours >= 24:  # Đủ 1 ngày (24 giờ)
            discount_rate = self.daily_discount
            discount_type = "Giảm giá theo ngày"
        
        # Tính số tiền giảm và giá cuối cùng
        discount_amount = base_price * discount_rate
        final_price = base_price - discount_amount
        
        # Tính toán thông tin bổ sung
        days = hours / 24
        months = hours / (24 * 30)
        
        return {
            "hours": hours,
            "days": round(days, 2),
            "months": round(months, 2),
            "hourly_rate": f"{self.hourly_rate:,} VND/giờ",
            "base_price": f"{base_price:,} VND",
            "discount_type": discount_type,
            "discount_rate": f"{discount_rate * 100}%",
            "discount_amount": f"{discount_amount:,} VND",
            "final_price": f"{final_price:,} VND",
            "savings": f"{discount_amount:,} VND"
        }
