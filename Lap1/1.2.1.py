# ===== PHẦN 1: CÁC PHÉP TOÁN TRÊN DANH SÁCH =====
danh_sach1 = [1, 3]
danh_sach2 = [5, 7]

# Cộng hai danh sách
danh_sach = danh_sach1 + danh_sach2
print("Kết quả cộng danh sách:", danh_sach)

# Nhân danh sách với 2 (lặp lại 2 lần)
danh_sach_gapdoi = 2 * danh_sach
print("Gấp đôi danh sách:", danh_sach_gapdoi)

# Lặp danh sách 2 lần (giống phép nhân)
print("Danh sách nhân 2 lần:", danh_sach * 2)

# Chia danh sách cho 2 -> KHÔNG HỢP LỆ trong Python (sẽ bị lỗi)
# print(danh_sach / 2)  # Dòng này sẽ gây lỗi, vì không chia danh sách được

print("-" * 40)

# ===== PHẦN 2: GHÉP DANH SÁCH BẰNG ZIP =====
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]

# Ghép 3 danh sách thành từng bộ (tuple)
anh_xa = list(zip(thu_tu, mon_hoc, diem_so))
print("Danh sách ghép bằng zip:")
print(anh_xa)

# Đưa vào tập hợp để loại bỏ trùng (set không giữ thứ tự)
tap_hop = set(anh_xa)
print("Chuyển sang tập hợp:")
print(tap_hop)

# Phân rã lại các phần từ zip
lay_TT, lay_monhoc, lay_diem = zip(*tap_hop)
print("Danh sách môn học sau phân rã:")
print(lay_monhoc)

print("-" * 40)

# ===== PHẦN 3: NỐI NHIỀU DANH SÁCH BẰNG itertools.chain =====
import itertools

tap_sinh = list(itertools.chain(range(4), range(5, 10), range(15, 20)))
print("Danh sách sinh bằng itertools.chain:")
print(tap_sinh)

print("-" * 40)

# ===== PHẦN 4: ZIP NHIỀU DANH SÁCH =====
bo_3 = list(zip(range(4), range(7, 12), reversed(range(11))))
print("Kết quả zip 3 danh sách:")
print(bo_3)
