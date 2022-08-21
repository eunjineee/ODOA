T = int(input())
for t in range(1, T+1):
    m = list(input())
    stack = []
    top = -1
    for i in range(len(m)):
        stack.append(m[i])
        top += 1
        if top >= 1:
            if stack[top] == stack[top-1]:
                stack.pop()
                stack.pop()
                top -= 2
    if len(stack) == 0:
        print(f'#{t} 0')
    else:
        print(f'#{t} {len(stack)}')