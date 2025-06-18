# Tim so lon nhat:
# caonhat = 0
# for i in [10, 7, 30, 2, 1]:
#     if i>caonhat:
#         caonhat = i
# print("cao nhat:", caonhat)
# 
#In ra danh sach ten:
# count = 0
# danhsachlop = ["Nguyen Van A", "Nguyen Van B", "Nguyen Thi C", "Tran Van D"]
# for i in danhsachlop:
#     count += 1
#     print(f"{count}. {i}")
# danhsachlop = ["Nguyen Van A", "Nguyen Van B", "Nguyen Thi C", "Tran Van D"]
# for idx, value in (danhsachlop):
#     print(f"STT: {idx+1}, Ho ten: {value}")

ds = [10,7,9,25,300,5,6,8,4,3,2,1]
solonnhat = 0
vitri = 0
for stt,giatri in enumerate(ds):
    if giatri > solonnhat:
        solonnhat = giatri
        vitri = stt
print("So lon nhat trong danh sach la:", solonnhat)
print("Vi tri cua so lon nhat:", vitri)

