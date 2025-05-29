from sympy import Symbol, solve
x = Symbol('x')
bieuthuc = x + 3 - 5
nghiem = solve(bieuthuc)
print("Nghiệm của phương trình x + 3 - 5 = 0 là:", nghiem)
bieuthuc2 = x**2 + 3 - 5
nghiemx = solve(bieuthuc2)
print("Nghiệm của phương trình x^2 + 3 - 5 = 0 là:", nghiemx)
print("Nghiệm 1:", nghiemx[0])
print("Nghiệm 2:", nghiemx[1])
