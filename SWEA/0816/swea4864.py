T = int(input())
for t in range(1,T+1):
    a = input()
    b = input()
    for j in range(len(b)-len(a)+1):
        for x in range(len(a)):
            if b[j+x] != a[x]:
                break
        else:
            print(f'#{t} 1')
            break
    else:
        print(f'#{t} 0')


'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''