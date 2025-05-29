from sympy import symbols
x= symbols('x')
y=symbols('y')
x=int(input('Mời nhấp số x: '))
y=int(input('Mời nhập số y: '))
s = x*y+y*x
print("Kết quả s là: ",s)

p= x*(x+x*2)
print("Kết quả p là: ",p)

o= (x+2)*(y+3)
print('Kết quả o là: ',o)

i= (x+2)*(y+3) + (x+2)*(x-3)
print("Kết quả i là: ",i)

