A, B, C = [int(input()) for _ in range(3)]

to = str(A * B * C)
di = {}

for j in range(10):
    di[j] = 0

for i in to:
    di[int(i)] += 1

for x in di:
    print(f'{di[x]}')