# 🚗 Smart Parking Management System (SPMS)

A Python-based Smart Parking Management System with role-based access, real-time slot monitoring, and fee calculation.

---

## 🎯 Objective

This system allows managing parking slots, checking vehicles in/out, calculating parking fees based on time, storing history, and generating reports. It supports 3 user roles:

- **Admin**: Configure parking lot, set pricing, view reports.
- **Parking Attendant**: Record vehicle entry/exit, update slot availability.
- **Vehicle Owner**: View available slots, check and pay parking fees.

---

## 🔐 Roles and Features

| Role | Features |
|------|----------|
| Admin | Manage slots, set hourly rates, export revenue reports |
| Parking Attendant | Check-in/out vehicles, update slots |
| Vehicle Owner | View available slots, pay parking fees |

---

## ✅ Task Checklist

### 🗂 Core Modules
- [ ] `main.py`: Command-line interface (CLI) menu
- [ ] `user.py`: Role and login simulation
- [ ] `slot.py`: Parking slot management **[📦 uses JSON]**
- [ ] `vehicle.py`: Vehicle information
- [ ] `transaction.py`: Check-in/out and fee calculation **[📦 uses JSON]**
- [ ] `data_handler.py`: JSON file read/write **[🔧 JSON helper functions]**
- [ ] `report.py`: Revenue statistics and reports **[📦 uses JSON]**

### 📂 JSON Data Files
- [ ] `data/slots.json`
- [ ] `data/vehicles.json`
- [ ] `data/transactions.json`

### 📸 Documentation
- [ ] Complete `README.md`
- [ ] System flowchart
- [ ] Program screenshots

---

## 🧑‍💻 Team Members & Responsibilities

| Member | Responsibility | Files |
|--------|----------------|--------|
| [You] | Team leader, integration, main menu | `main.py` |
| Member 1 | Role and login management | `user.py` |
| Member 2 | Parking slot module | `slot.py` |
| Member 3 | Vehicle and transaction logic | `vehicle.py`, `transaction.py` |
| Member 4 | Data persistence and report generation | `data_handler.py`, `report.py` |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Programming language |
| Git + GitHub | Version control, team collaboration |
| VS Code | Code editor |
| JSON | Data storage format |
| draw.io | Flowchart design |
| CSV (optional) | Report export format |

---
🔐 1. ADMIN – Quản trị viên
Có quyền cao nhất, được phép cấu hình toàn bộ hệ thống.

✅ Quyền của Admin:
Chức năng	Mô tả
Cấu hình bãi đỗ	Thiết lập tổng số slot, khu vực, loại xe
Quản lý chỗ đỗ	Thêm/sửa/xóa slot
Đặt mức phí	Giá theo giờ, lũy tiến, phí mở đầu
Xem báo cáo	Thống kê doanh thu, lượng xe
Xuất file	Báo cáo dưới dạng CSV hoặc TXT
Xóa dữ liệu cũ	Ví dụ: transaction > 30 ngày

👷 2. PARKING ATTENDANT – Nhân viên trông xe
Có quyền thao tác với xe và chỗ đỗ nhưng không được cấu hình hệ thống.

✅ Quyền của Attendant:
Chức năng	Mô tả
Check-in xe	Gán xe vào slot còn trống, ghi thời gian
Check-out xe	Trả slot, tính phí, ghi thời gian ra
Xem slot trống	Hiển thị slot đang còn khả dụng
Kiểm tra xe đang đỗ	Danh sách xe chưa check-out
Ngăn đăng ký trùng	Không cho xe vào nếu chưa check-out trước đó
In hóa đơn .txt	Sau check-out

🚗 3. VEHICLE OWNER – Chủ phương tiện
Giao diện thân thiện, chỉ cho phép các chức năng cơ bản như xem, đăng ký và thanh toán.

✅ Quyền của Owner:
Chức năng	Mô tả
Tìm chỗ trống	Xem các slot có thể vào
Đăng ký xe	Tự nhập biển số để hệ thống check-in
Xem phí đỗ xe	Tính phí theo thời gian đã đỗ
Thanh toán	Hiển thị hóa đơn
Xem lịch sử	Thời gian đã đỗ trước đó, số tiền đã trả



## 🌟 Extended Features (Grouped)

### 🧑‍🎓 Basic (Terminal-friendly)
- [ ] Search vehicle by license plate
- [ ] Export receipt as `.txt`
- [ ] Show total fee paid by a vehicle
- [ ] Prevent duplicate check-in

### 💡 Practical Use-Cases
- [ ] List vehicles currently parked
- [ ] Sort slots by usage frequency
- [ ] Revenue per day/week
- [ ] Vehicle check-in/out history
- [ ] Use real system time (datetime)
- [ ] Show available slots

### 🚀 Advanced Professional Features
- [ ] Average parking time per vehicle
- [ ] Vehicle type classification (car, bike, etc.)
- [ ] Base fee + hourly fee
- [ ] Tiered pricing (e.g., different after 2 hours)
- [ ] Remove old records (>30 days)
- [ ] Generate QR-style text for tickets
- [ ] Log user actions in a log file
- [ ] Peak hour analytics

---

## 🧭 Development Plan

| Phase | Week | Tasks |
|-------|------|-------|
| Week 1 | Planning, repo setup | Create README, branches, module stubs |
| Week 2 | Implement modules | Slot, Transaction, Roles |
| Week 3 | Integration & testing | Connect functions and finalize logic |
| Week 4 | Final reports | Flowchart, screenshots, documentation |

---

## 🧱 Folder Structure

```
smart-parking-system/
├── main.py
├── user.py
├── slot.py              📦
├── vehicle.py
├── transaction.py       📦
├── data_handler.py      🔧
├── report.py            📦
├── data/
│   ├── slots.json
│   ├── vehicles.json
│   └── transactions.json
├── README.md
└── .gitignore
```

📦 = Uses JSON | 🔧 = JSON utility module

---

## 🚀 How to Run

```bash
git clone https://github.com/your-username/smart-parking-system.git
cd smart-parking-system
python main.py
```

---

## 📦 Dependencies

- Python 3.x
- No third-party libraries required (`json`, `datetime`, `os` from standard library)

---

## 📌 Future Improvements

- [ ] Online reservation system
- [ ] GUI (Tkinter / Flask)
- [ ] Admin login system
- [ ] SMS/Email notifications
