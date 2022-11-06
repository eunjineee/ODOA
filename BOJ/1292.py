a, b = map(int, input().split())
ans = []

for i in range(1,50):
    for j in range(i):
        ans.append(i)
answer = sum(ans[a-1:b])
print(answer)