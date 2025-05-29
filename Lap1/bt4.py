from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5
nghiem = solve((pt1, pt2), dict=True)
print(nghiem)
ket_qua = nghiem[0]
x_nghiem = ket_qua[x]
y_nghiem = ket_qua[y]
print(f"Nghiệm của hệ là: x = {x_nghiem}, y = {y_nghiem}")
