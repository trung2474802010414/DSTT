import numpy as np
A = np.array([
    [1, 0, 1, 0, 1],
    [2, 0, 0, 1, 2],
    [0, 1, 0, 0, 1],
    [2, 1, 0, 1, 0],
    [1, 2, 2, 0, 0]
])

B = np.array([
    [1, 2, 2, 2, 1],
    [0, 1, 1, 2, 2],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 2, 1, 0, 0]
])

C = np.array([
    [0, 1, 0, 2, 0],
    [1, 0, 1, 0, 2],
    [2, 1, 0, 1, 1],
    [0, 2, 1, 0, 2],
    [1, 1, 2, 2, 1]
])

D = np.array([
    [5, 3, 0, 1, 0],
    [1, 2, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [3, 1, 1, 0, 0],
    [5, 0, 0, 0, 0]
])

E = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
])

def tinh_diem_nguy_co(*matran_list):
    return sum(matran_list)

def vi_tri_an_toan(diem_nguy_co):
    return diem_nguy_co <= 5
#a
diem_a = tinh_diem_nguy_co(E)
an_toan_a = vi_tri_an_toan(diem_a)
print("a/ Vị trí an toàn (chống lộ bí mật):\n", an_toan_a.astype(int))
#b
diem_b = tinh_diem_nguy_co(A, D)
an_toan_b = vi_tri_an_toan(diem_b)
print("b/ Vị trí an toàn (tránh cháy rừng và dịch bệnh):\n", an_toan_b.astype(int))
#c
diem_c = tinh_diem_nguy_co(B, D)
an_toan_c = vi_tri_an_toan(diem_c)
print("c/ Vị trí an toàn (tránh lũ và dịch bệnh):\n", an_toan_c.astype(int))
#d
diem_d = tinh_diem_nguy_co(B, C, D, A)
an_toan_d = vi_tri_an_toan(diem_d)
print("d/ Vị trí an toàn mùa mưa:\n", an_toan_d.astype(int))
#e
diem_e = tinh_diem_nguy_co(A, B, C, D, E)
an_toan_e = vi_tri_an_toan(diem_e)
print("e/ Vị trí an toàn trong 8 tháng:\n", an_toan_e.astype(int))

def in_ma_tran_ten(ma_tran, ten):
    print(f"{ten}:\n{ma_tran.astype(int)}\n")

in_ma_tran_ten(an_toan_a, "a/ An toàn ngắn hạn (lộ bí mật)")
in_ma_tran_ten(an_toan_b, "b/ Tập huấn thời bình")
in_ma_tran_ten(an_toan_c, "c/ Trú quân mùa khô")
in_ma_tran_ten(an_toan_d, "d/ Trú quân mùa mưa")
in_ma_tran_ten(an_toan_e, "e/ An toàn quanh năm (8 tháng)")
