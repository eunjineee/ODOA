import sys
N = int(sys.stdin.readline())
stack = []

for n in range(N):
    a= list(sys.stdin.readline().split())
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if len(stack) == 0 :
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])