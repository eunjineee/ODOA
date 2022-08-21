import sys
sys.stdin = open('input.txt')

T = int(input())   #10:34

for t in range(1,T+1):
    K, N, M = map(int, input().split())
    mli = [0]*(N+1)
    Mli = list(map(int, input().split()))
    ch = 0
    go = K
    hu = 0
    for m in Mli:
        mli[m] = 1
    Mli.append(N)

    for n in range(1,N+1):
        if mli[n] == 0:
            go -= 1
        elif mli[n] == 1:
            go -= 1
            if go < 0:
                ch = 0
                break
            if go >= Mli[hu+1] - Mli[hu]:
                hu += 1
            else:                            #go <Mli[i+1] - Mli[i]
                go = K
                ch += 1
                hu += 1

    print(f'#{t} {ch}')