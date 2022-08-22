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
print(*nums,*stack,sep="")