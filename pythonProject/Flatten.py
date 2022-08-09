import sys
sys.stdin = open('input.txt')

for i in range(1,11):
    N = int(input())
    nums = list(map(int, input().split()))
    count = [0] * 101
    nmax = nmin = nums[0]

    for num in nums:
        count[num] += 1
        if nmax < num:
            nmax = num
        if nmin > num:
            nmin = num
    while j < N:
        if count[nmax] == 1:
            count[nmax] -= 1
            count[nmax-1] += 1
            nmax -= 1
            if count[nmin] >= 1:
                count[nmin] -= 1
                count[nmin+1] += 1
                nmin += 1
            else:
                count[nmin] -= 1
                count[nmin+1] += 1
        else:
            count[nmax] -= 1
            count[nmax + 1] += 1
            if count[nmin] >= 1:
                count[nmin] -= 1
                count[nmin+1] += 1
                nmin += 1
            else:
                count[nmin] -= 1
                count[nmin+1] += 1
        if nmax - nmin <= 1:
            break
        j += 1
    to = nmax - nmin
print(f'#{i} {to}')