from sympy import symbols, pprint, init_printing, factor

# In biểu thức theo thứ tự ngược biến (y trước x)
init_printing(order='rev-lex')

# Khai báo biến
x, y = symbols('x y')

# Tạo biểu thức
bieuthuc = x**2 - 2*x*y + y**2

# In biểu thức ban đầu
print("Biểu thức ban đầu:")
pprint(bieuthuc)

# Rút gọn biểu thức
bieuthuc1 = factor(bieuthuc)

# In biểu thức sau khi rút gọn
print("\nBiểu thức sau khi rút gọn:")
pprint(bieuthuc1)
