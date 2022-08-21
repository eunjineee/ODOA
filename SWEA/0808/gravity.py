N = int(input())
for i in range(N):
    nacli = []
    so = int(input())
    nums = list(map(int, input().split()))
    top = 0
    for a in range(so):
        nac = 0 
        for b in range(a+1, so):
            if nums[a] > nums[b]:   #처음잡은수 > 다음수
                nac += 1           #낙차 +1
        if nac > top:
            top = nac

    print(f'#{i+1} {top}')

'''
7
4
2
0
0
6
0
7
0
'''