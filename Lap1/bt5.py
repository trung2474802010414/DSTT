import numpy as np
M1 = np.array([[9, 12], [23, 30]])
print("M1 =\n", M1)
u = np.array([2, 1])
print("Vector u =", u)
tichM1 = M1.dot(u)
print("M1.dot(u) =", tichM1)  
tichuM1 = u.dot(M1)
print("u.dot(M1) =", tichuM1) 
print("np.dot(u, M1) =", np.dot(u, M1))  

#THỰC HÀNH VỚI MẢNG NUMPY 
mat1 = np.zeros((5,5))
print("mat1 (zeros):\n", mat1)
mat2 = np.ones((5,5))
print("mat2 (ones):\n", mat2)
mat3 = mat1 + 2 * mat2
print("mat3 = mat1 + 2 * mat2:\n", mat3)
mat4 = mat3
mat3[3][2] = 10
print("mat3 sau khi đổi mat3[3][2] = 10:\n", mat3)
print("mat4 cũng thay đổi theo (vì là tham chiếu):\n", mat4)
mat5 = np.copy(mat3)
mat3[3][2] = 20 
print("mat3 sau khi đổi tiếp mat3[3][2] = 20:\n", mat3)
print("mat5 không bị ảnh hưởng:\n", mat5)
#rỗng
mat6 = np.empty((4,5))
print("mat6 (empty - giá trị rác không xác định):\n", mat6)
#đơn vị
mat7 = np.identity(4)
print("mat7 (identity):\n", mat7)
#random
mat8 = np.random.rand(4,5)
print("mat8 (random values in [0,1)):\n", mat8)
