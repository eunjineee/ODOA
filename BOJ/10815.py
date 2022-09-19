n = int(input())
snum = list(map(int, input().split()))
m = int(input())
checkli = list(map(int, input().split()))

snum.sort()

def eeejin(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid +1

for j in checkli:
    if eeejin(snum, j, 0, n-1):
        print(1,end=' ')
    else:
        print(0,end= ' ')