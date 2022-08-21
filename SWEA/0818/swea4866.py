T = int(input())

for t in range(1,T+1):
    name = list(input())
    nameli = []
    ans = 1
    for i in range(len(name)):
        if name[i] == '(':
            nameli.append(1)
        elif name[i] == ')':
            if len(nameli) !=0:
                if nameli[-1] != 1:
                    ans = 0
                    break
                else:
                    nameli.pop()
            else:
                ans = 0
                break
        elif name[i] == '{':
            nameli.append(2)

        elif name[i] == '}':
            if len(nameli) != 0:
                if nameli[-1] != 2:
                    ans = 0
                    break
                else:
                    nameli.pop()
            else:
                ans = 0
                break

    if len(nameli) == 0 and ans != 0:
        ans = 1
    else:
        ans = 0

    print(f'#{t} {ans}')
