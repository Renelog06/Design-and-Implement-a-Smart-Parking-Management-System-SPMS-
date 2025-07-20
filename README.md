# 🚗 Smart Parking Management System (SPMS)

A Python-based Smart Parking Management System with role-based access, real-time slot monitoring, and fee calculation.

---

## 🎯 Objective

This system allows managing parking slots, checking vehicles in/out, calculating parking fees based on time, storing history, and generating reports. It supports 3 user roles:

- **Admin**: Configure parking lot, set pricing, view reports.
- **Parking Attendant**: Record vehicle entry/exit, update slot availability.
- **Vehicle Owner**: View available slots, check and pay parking fees.

---
#File_need
### 🗂 Core Modules
- [x] `main.py`: Command-line interface (CLI) menu | Phú Anh
- [x] `auth.py`: Login | Phú Anh
- [x] `data_handler.py`: JSON file read/write **[🔧 JSON helper functions]** | Nhựt Trường
- [x] `user.py`: Role and login simulation| Phi Trường
- [x] `slot.py`: Parking slot management **[📦 uses JSON]** |Hiếu
- [x] `vehicle.py`: Vehicle information | Hưng
- [x] `transaction.py`: Check-in/out and fee calculation **[📦 uses JSON]** | Hưng
- [x] `report.py`: Revenue statistics and reports **[📦 uses JSON]** | Nhựt Trường


### 📂 JSON Data Files
- [x] `data/slots.json`
- [x] `data/vehicles.json`
- [x] `data/transactions.json`
- [x] `data/users.json`

### 📸 Documentation
- [x] Complete `README.md`
- [x] System flowchartflowchart | https://www.mermaidchart.com/app/projects/48b8d78c-f824-49f7-9495-f6d22a6b15d6/diagrams/1b35f458-33a6-4991-826e-6c2debac533c/version/v0.1/edit
---
# ✅ Task Checklist
## 🧑‍💻 Team Members & Responsibilities

| Member |TMP Responsibility | Core Responsibility | Rate |
|--------|----------------|------------------------|------|
| Phu Anh ( Team_leader) | View parking status | main, auth | 20% |
| Phi Truong |  View vehicle entry/exit history| user | 20% |
| Hieu | Set parking fees | slot | 20% |
| Hung | Reset/clear data before configuring the parking lot | transaction, vehicle  | 20% |
| Nhut Truong  | Search for vehicles currently parked | data, report | 20% |

---
## 🔐 Roles & Features and Bugs
Below are the permissions and features available for each role:
Admin:
- Configure parking lot settings. [x]
- Set parking fees:[x]
  1.Hourly fee: 2,000 VND/hour.
  2.Daily fee: calculated as 24 hours * hourly rate.
     > If parking exceeds 1 day: apply 10% additional fee.
     > If parking exceeds 28 days: apply 20% monthly discount.
- Add or delete parking slots. [x]

Parking Attendant:
- (not prioritized) Search for vehicles currently parked.[x]
- Check in/out vehicles.[x]
- (not prioritized) View vehicle entry/exit history.[x]
- (not prioritized) View parking status (occupied slots with vehicle ID and available slots).[x]

Vehicle Owner:
- (available slots) (not prioritized) View parking status. [x]
- Check in vehicles. [x]
  1.Enter desired parking duration (hours/days).
  2.System calculates the expected fee based on time.
### BUGS
- Reset/clear data before configuring the parking lot [x]
- Handle report generation and traceback errors [x]
- Update user module (currently using mock file) [xx]

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Programming language |
| Git + GitHub | Version control, team collaboration |
| VS Code | Code editor |
| JSON | Data storage format |
| mermaidchart with AI| Flowchart design | 

---

## 🌟 Extended Features (Grouped)
---

## 🧭 Development Plan

| Phase | Week | Tasks |
|-------|------|-------|
| Week 1 | Planning, repo setup | Create README, branches, module stubs |
| Week 2 | Implement modules | Slot, Transaction, Roles |
| Week 3 | Integration & testing | Connect functions and finalize logic |
| Week 4 | Final reports | Flowchart, screenshots, documentation |

---

## 🚀 How to Run

```bash
git clone https://github.com/Renelog06/Design-and-Implement-a-Smart-Parking-Management-System-SPMS-.git
cd Design-and-Implement-a-Smart-Parking-Management-System-SPMS-
python main.py
```
---

## 📦 Dependencies

- Python 3.10
- No third-party libraries required (`json`, `datetime`, `os` from standard library)


