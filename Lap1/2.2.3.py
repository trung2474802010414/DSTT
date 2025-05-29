from sympy import Symbol, simplify, sin, cos

# Định nghĩa biến
x = Symbol('x')
y = Symbol('y')

# Định nghĩa biểu thức: x**2 - x*y + y**2
bieuthuc = x**2 - x*y + y**2
print("Biểu thức ban đầu:")
print(bieuthuc)
giatri = bieuthuc.subs({x: 3, y: 2})
print("\nGiá trị khi thay x = 3, y = 2:")
print(giatri)
print("\nKiểm tra x và y sau thay thế:")
print(x)
print(y)

#Thực hành
#Tình huống 1:
print("\nTình huống 1: Thay theo thứ tự x = 3, y = x")
giatri1 = bieuthuc.subs({x: 3, y: x})
print("Giá trị biểu thức:")
print(giatri1)
giatri1_alt = bieuthuc.subs({x: 3, y: x})
print("Cách thay khác:")
print(giatri1_alt)

# Tình huống 2:
print("\nTình huống 2: Thay theo thứ tự x = y, y = 3")
giatri2 = bieuthuc.subs({x: y, y: 3})
print("Giá trị biểu thức:")
print(giatri2)
giatri2_alt = bieuthuc.subs({x: y}).subs({y: 3})
print("Cách thay khác:")
print(giatri2_alt)

#Tình huống 3: 
print("\nTình huống 3: Thay theo thứ tự y = x, rồi x = 3")
giatri3 = bieuthuc.subs({y: x}).subs({x: 3})
print("Giá trị biểu thức:")
print(giatri3)

#simplify
bieuthuc_moi = bieuthuc.subs({x: 1 - y})
print("\nBiểu thức sau khi thay x = 1 - y:")
print(bieuthuc_moi)
dongian = simplify(bieuthuc_moi)
print("\nBiểu thức đã rút gọn:")
print(dongian)

# simplify với lượng giác
x = Symbol('x')
y = Symbol('y')
bt = sin(x)*cos(y) + cos(x)*sin(y)
print("Biểu thức ban đầu:")
print(bt)
bt_moi = simplify(bt)
print("Biểu thức sau khi rút gọn:")
print(bt_moi)
