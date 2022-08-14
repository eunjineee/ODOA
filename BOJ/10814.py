n = int(input())
names = []

for _ in range(n):
    age = input().split()
    names.append((int(age[0]), age[1]))

names = sorted(names, key=lambda x : x[0])

for i in names:
    print(i[0], i[1])