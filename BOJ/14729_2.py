n = int(input())
array = []
for _ in range(n):
    array.append(input())
array = sorted(array)
for data in array[:7]:
    print(data)