import numpy as np


arr = np.arange(11)

print(arr)

print(arr[:7])

arr[0:3] = 100

print(arr)

arr = np.arange(11)

slice_of_arr = arr[0:5]

slice_of_arr[:] = 99

print(arr)

# Reference가 아닌 독자적인 Copy값을 가짐
arr_copy = arr.copy()

arr_copy[:5] = 21

print(arr_copy)
print(arr)

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

print(arr_2d)

# == arr_2d[0][2]
print(arr_2d[0, 2])

print(arr_2d[:2, 1:])

arr = np.arange(1, 11)

print(arr > 5)

print(arr[arr > 5])

arr_2d = np.arange(50).reshape(5, 10)

print(arr_2d)

print(arr_2d[1:3, 3:5])
