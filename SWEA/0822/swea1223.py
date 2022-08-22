for t in range(10):
    stack = []
    nums = []
    n = int(input())
    li = list(input())
    for i in li:
        if  i == '+':
            try:
                if len(stack) != 0:
                    while stack[-1] == '*' or  stack[-1] == '+':
                        nums.append(stack.pop())
                stack.append(i)
            except IndexError:
                stack.append(i)
                continue
        elif  i == '*':
            try:
                if len(stack) != 0:
                    while stack[-1] == '*' :
                        nums.append(stack.pop())
                stack.append(i)
            except IndexError:
                stack.append(i)
                continue
        else:
            nums.append(int(i))
    stack = stack[::-1]
    hui = nums + stack

    total = []
    for j in hui:
        if j == '+':
            o = total.pop()
            k = total.pop()
            total.append(k+o)
        elif j == '*':
            o = total.pop()
            k = total.pop()
            total.append(k * o)
        else:
            total.append(j)
    print(f'#{t+1} ',end='')
    print(total[0])