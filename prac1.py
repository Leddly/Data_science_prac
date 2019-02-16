import numpy as np


my_list = [1, 2, 3, 4]
arr = np.array(my_list)

print(arr)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(np.array(my_mat))

print(np.arange(0, 10, 2))

print(np.zeros((5, 5)))

print(np.ones((5, 3)))

# (start, end, num) 시작부터 끝나는 숫자까지 정해진 갯수로 나눈 값으로 Array 생성
print(np.linspace(0, 5, 4))

print(np.eye(4))

# 0 ~ 1까지 숫자로 Array 랜덤생성 (균일한 확률로 생성불가)
print(np.random.rand(5, 5))

# 가우시안 표준 정규분포
print(np.random.randn(2, 4))

# start부터 end 사이의 num개수의 숫자 Array 생성
print(np.random.randint(2, 4, 5))

randarr = np.random.randint(0, 50, 25)

print(randarr)

print(randarr.reshape(5, 5))

print(randarr.max())
print(randarr.min())

# 최대값 위치 return
print(randarr.argmax())
# 최소값 위치 return
print(randarr.argmin())

arr = np.arange(25)

arr = arr.reshape(5, 5)
print(arr)
