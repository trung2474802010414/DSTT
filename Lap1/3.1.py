import numpy as np
vec1 = np.array([1., 3., 5.])
print("vec1 * 2:", vec1 * 2)
print("vec1 * vec1:", vec1 * vec1)
print("vec1 / 2:", vec1 / 2)
print("vec1 + vec1:", vec1 + vec1)

vec2 = np.array([2., 4.])
try:
    print("vec1 + vec2:", vec1 + vec2)
except ValueError as e:
    print("vec1 + vec2 Error:", e)

vec3 = np.array([2., 4., 6.])
print("vec1 + vec3:", vec1 + vec3)
print("vec1 / vec3:", vec1 / vec3)
print("vec1 * vec3:", vec1 * vec3)
print("2 * vec1 + 5 * vec3:", 2 * vec1 + 5 * vec3)
print("vec3[2]:", vec3[2])

vec4 = np.linspace(0, 20, 5)
print("vec4 (linspace):", vec4)

vec5 = np.zeros(5)
print("vec5 (zeros):", vec5)

vec6 = np.ones(5)
print("vec6 (ones):", vec6)

vec7 = np.empty(5)
print("vec7 (empty):", vec7)
rand_vec1 = np.random.rand(5)
print("rand_vec1:", rand_vec1)
rand_vec2 = np.random.random(5)
print("rand_vec2:", rand_vec2)

v = np.array([[1., 3., 5.]])
print("np.sum(v):", np.sum(v))
print("v.shape:", v.shape)
print("v.transpose():\n", v.transpose())
v1 = v[0]
v1[0] = 5
print("v1 sau khi gán:", v1)
print("v1[1:3]:", v1[1:3])
v1[:2] = [1, 2]
print("v1 sau khi gán lại [:2]:", v1)
v3 = 2 + v1[2] + v1[1] * 3
print("v3 =", v3)
print("np.sqrt(7.):", np.sqrt(7.))
print("np.cos(7.):", np.cos(7.))
print("np.sin(7.):", np.sin(7.))
v1 = np.array([4., 6.])  
print("np.dot(v1, v3):", np.dot(v1, v3))
print("v1.dot(v3):", v1.dot(v3))
print("v3.dot(v1):", np.dot(v3, v1)) 
