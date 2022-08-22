T = int(input())

for t in range(T):
    stack = []
    nums = []
    li = list(input())
    for i in li:
        if i == '+' or i == '-' or i == '/' or i == '*':
            stack.append(i)
        else:
            nums.append(int(i))
    stack = stack[::-1]
    print(f'#{t+1} ',end='')
    print(*nums,*stack, sep="")