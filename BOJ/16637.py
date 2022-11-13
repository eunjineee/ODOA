n = int(input())
strs = list(input())

nums = []
p = []

ans = -float('inf')

for i in strs:
    if i.isdigit():
        nums.append(i)
    else:
        p.append(i)

def f(n, total):
    global ans

    if n == len(p):
        ans = max(ans, int(total))
        return
    
    first = str(eval(total + p[n] + nums[n+1]))
    f(n+1, first)
    
    if n+1 < len(p):
        second = str(eval(nums[n+1] + p[n+1] + nums[n+2]))
        second = str(eval(total + p[n]+ second))
        f(n+2, second)

f(0, nums[0])
print(ans)

