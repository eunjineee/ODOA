n = input()
d = {}
for i in range(97,123):
    d[i] = -1

for j in range(len(n)):
    d[ord(n[len(n)-1-j])] = len(n)-1-j

for x in range(97,123):
    print(d[x],end=' ')