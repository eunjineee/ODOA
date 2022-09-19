import sys
sys.stdin= open('input.txt')

n = int(input())

nums = []
for i in range(n,0,-1):
    nums.append(i)

stack = []

for j in range(n):
    a = int(input())
    if a in nums:
        if nums[-1] == a:
            print('-')
            nums.pop()
        else:
            while a in nums:
                stack.append(nums.pop())
                print('+')
            stack.pop()
            print('-')
    else:
        if stack[-1] == a:
            print('-')
            stack.pop()
        else:
            while a in stack:
                nums.append(stack.pop())
                print('+')
            nums.pop()
            print('+')




'''
5
1
2
5
3
4

8
4
3
6
8
7
5
2
1
'''