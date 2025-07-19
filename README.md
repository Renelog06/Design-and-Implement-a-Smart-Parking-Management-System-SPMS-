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
- [x] `main.py`: Command-line interface (CLI) menu
- [x] `auth.py`: Login
- [x] `user.py`: Role and login simulation
- [x] `slot.py`: Parking slot management **[📦 uses JSON]**
- [x] `vehicle.py`: Vehicle information
- [x] `transaction.py`: Check-in/out and fee calculation **[📦 uses JSON]**
- [x] `data_handler.py`: JSON file read/write **[🔧 JSON helper functions]**
- [x] `report.py`: Revenue statistics and reports **[📦 uses JSON]**

### 📂 JSON Data Files
- [x] `data/slots.json`
- [x] `data/vehicles.json`
- [x] `data/transactions.json`
- [x] `data/users.json`

### 📸 Documentation
- [x] Complete `README.md`
- [x] System flowchartflowchart | https://lucid.app/lucidchart/6e7376f1-f272-4037-93f4-e2eb8ff7d5be/edit?invitationId=inv_9ae8547b-71dd-494b-925a-b7a92cfb239d&page=0_0#
---
# ✅ Task Checklist
## 🧑‍💻 Team Members & Responsibilities

| Member | Responsibility | 
|--------|----------------|
| Phu Anh ( Team_leader) | View parking status  | 
| Phi Truong |  View vehicle entry/exit history|
| Hieu | Set parking fees |
| Hung | Reset/clear data before configuring the parking lot |
| Nhut Truong  | Search for vehicles currently parked |

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
| Lucidchart | Flowchart design | 

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
git clone https://github.com/your-username/smart-parking-system.git
cd smart-parking-system
python main.py
```
---

## 📦 Dependencies

- Python 3.10
- No third-party libraries required (`json`, `datetime`, `os` from standard library)


