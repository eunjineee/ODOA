def pre(n):                                 # 전위순회
    if n:
        print(par[n], end='')
        pre(ch1[n])
        pre(ch2[n])

def ino(n):                                 # 중위순회
    if n:
        ino(ch1[n])
        print(par[n], end='')
        ino(ch2[n])

def post(n):                                 # 후위순회
    if n:
        post(ch1[n])
        post(ch2[n])
        print(par[n], end='')

for S in range(1, 11):
    V = int(input())                        # 정점 개수, 마지막 정점 번호
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    par = [0] * (V + 1)                     # 노드에 해당하는 문자를 넣을 리스트

    for H in range(V):
        lst = input().split()
        if lst[1] != '.':                   # 자손이 .이 아닐 때 
            ch1[lst[0]] = lst[2]
        elif lst[2] != '.':                 # 자손이 하나일 때 
            ch2[lst[0]] = lst[3]

        par[lst[0]] = lst[1]

    print(f'#{S}', end=' ')
    pre(1)
    print()
    ino(1)
    print()
    post(1)
