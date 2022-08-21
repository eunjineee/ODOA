for i in range(10):
        
    T = input()
    pat = input()
    sou = input()
    num = 0
    for idx in range(len(sou)-len(pat) + 1):
        for j in range(len(pat)):
            if sou[idx + j] != pat[j]:
                break
        else:
            num+= 1
    print(f'#{T} {num}')