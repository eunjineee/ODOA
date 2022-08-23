n =int(input())

i = 1
while n > i: 
    n -= i
    i += 1


if i % 2 == 1:
    nums=(i-n+1,n)
else:    
    nums=(n,i-n+1)

print(f'{nums[0]}/{nums[1]}')