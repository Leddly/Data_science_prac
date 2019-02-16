import numpy as np


arr = np.arange(0, 11)

# array1 + array2 = for x in len(array1): result.append(array1[x] + array2[x])
print(arr + arr)

print(arr * arr)

print(arr - 100)

print(arr/2)

print(arr/arr)

print(1/arr)

print(arr**3)

#squareroot
print(np.sqrt(arr))

print(np.max(arr))

print(np.sin(arr))

print(np.tan(arr))

print(np.zeros(10))

print(np.ones(10))

print(np.eye(5))

print(np.arange(10, 51))

print(np.arange(10, 51, 2))

print(np.arange(0, 9).reshape(3, 3))

print(np.eye(3))

print(np.random.rand(1))

print(np.random.randn(25).reshape(5, 5))

# np.arange(1, 101).reshape(10, 10) / 100
# np.linspace(0.01, 1.01, 0.01).reshape(10, 10)
print(np.arange(0.01, 1.01, 0.01).reshape(10, 10))

print(np.linspace(0, 1, 20))

mat = np.arange(1, 26).reshape(5, 5)
mat2 = mat[2:, 1:].copy()

print(mat)
print(mat2)

# standard deviation
print(mat.std())

print(mat.sum())

print(mat.sum(axis=0))
