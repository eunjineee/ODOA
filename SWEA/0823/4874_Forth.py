T = int(input())

for t in range(T):
    hui = list(input().split())
    total = []
    for j in hui:
        try :
            if j == '+':
                o = total.pop()
                k = total.pop()
                total.append(k + o)
            elif j == '*':
                o = total.pop()
                k = total.pop()
                total.append(k * o)
            elif j == '/':
                o = total.pop()
                k = total.pop()
                total.append(k // o)
            elif j == '-':
                o = total.pop()
                k = total.pop()
                total.append(k - o)
            elif j == '.':
                if len(total) == 1:
                    print(f'#{t + 1} {total[0]}')
                else:
                    print(f'#{t + 1} error')
                break
            else:
                total.append(int(j))
        except:
            print(f'#{t + 1} error')
            break