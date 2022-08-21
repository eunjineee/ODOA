N = int(input())
stack = []
for n in range(N):
    a = input()
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(f'#{n} 1')
        else:
            if len(stack) == 0:
                print(f'#{n} -1')
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print(f'#{n} 1')
    else:
        print(f'#{n} -1')