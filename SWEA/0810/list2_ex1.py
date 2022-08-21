N = 3
M =4

arr1 = [0] * N

arr2 = [[0] * M for _ in range(N)]
print(arr2)

arr3 = [[0]*M]*N
print(arr3)
arr3[0][0] = 1
print(arr3)