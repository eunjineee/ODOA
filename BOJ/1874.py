import sys
sys.stdin= open('input.txt')
input = sys.stdin.readline
n = int(input())

nums = []
for i in range(n,0,-1):
    nums.append(i)

stack = []
total = []

for j in range(n):
    a = int(input())
    if a in nums:
        while a in nums:
            stack.append(nums.pop())
            total.append('+')
        stack.pop()
        total.append('-')
    elif len(stack) > 0 and stack[-1] == a:
        total.append('-')
        stack.pop()
    elif len(stack) > 0 and stack[-1] != a:
        print('NO')
        exit()

for k in total:
    print(k)



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