def pre(n):                                 # 전위순회
    if n:
        preli.append(par[n])
        pre(ch1[n])
        pre(ch2[n])

def ino(n):                                 # 중위순회
    if n:
        ino(ch1[n])
        inoli.append(par[n])
        ino(ch2[n])

def post(n):                                 # 후위순회
    if n:
        post(ch1[n])
        post(ch2[n])
        postli.append(par[n])

N = int(input())                        # 정점 개수, 마지막 정점 번호
ch1 = [0] * (N + 1)
ch2 = [0] * (N + 1)
par = [0] * (N + 1)                     # 노드에 해당하는 문자를 넣을 리스트

for _ in range(N):
    root, left, right = input().split()
    par[ord(root)-64] = root
    if left != '.':
        ch1[ord(root)-64] = ord(left)-64
    if right != '.':
        ch2[ord(root)-64] = ord(right)-64

preli = []
inoli = []
postli = []
pre(1)
ino(1)
post(1)

print(*preli, sep= '')
print(*inoli, sep= '')
print(*postli, sep= '')
