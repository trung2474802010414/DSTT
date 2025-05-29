from sympy import Symbol, factor, expand
x = Symbol('x')
y = Symbol('y')
x=int(input('Mời nhập số nguyên x: '))
y=int(input('Mời nhập số nguyên y: '))
bieuthuc = x**3 - y**3
ket_qua_factor = factor(bieuthuc)
print("Kết quả dùng factor():", ket_qua_factor)
bieuthuc = (x - y)*(x**2 + x*y + y**2)
ket_qua_expand = expand(bieuthuc)
print("Kết quả dùng expand():", ket_qua_expand)