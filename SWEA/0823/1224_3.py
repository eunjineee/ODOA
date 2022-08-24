for t in range(10):
    stack = []
    nums = []
    li = list(input())
    for i in li:
        if i == '(':
            stack.append(i)
        elif  i == '+' or i == '-':
            try:
                if len(stack) != 0:
                    while stack[-1] == '*' or  stack[-1] == '/' or stack[-1] == '-' or  stack[-1] == '+':
                        nums.append(stack.pop())
                stack.append(i)
            except IndexError:
                stack.append(i)
                continue
        elif i == '/' or i == '*':
            try:
                if len(stack) != 0:
                    while stack[-1] == '*' or  stack[-1] == '/':
                        nums.append(stack.pop())
                stack.append(i)
            except IndexError:
                stack.append(i)
                continue
        elif i == ")":
            while stack[-1] != '(':
                nums.append(stack.pop())
            stack.pop()
        else:
            nums.append(i)
    stack = stack[::-1]
    hui = nums + stack

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
            else:
                total.append(int(j))
        except:
            ans = "ROCK"
            break
    if len(total) == 1:
        ans = total[0]
    else:
        ans = "ROCK"
    print(ans)
