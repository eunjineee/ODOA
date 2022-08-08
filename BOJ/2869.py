a,b,v = map(int,input().split())
i = 0

if (v-a)%(a-b) != 0:
    print((v-a)//(a-b)+1)