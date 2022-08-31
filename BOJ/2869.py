a,b,v = map(int,input().split())
num = 1
num += (v-a)//(a-b)
j = (v-a) % (a-b)

if j > 0:
    num += 1

print(num)