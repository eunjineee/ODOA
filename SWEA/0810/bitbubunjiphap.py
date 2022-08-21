arr = [1, 2, 3]

n= len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):   #true number 1 give
            print(arr[j], end=', ')
    print()
print()
