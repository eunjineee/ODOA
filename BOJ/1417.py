import heapq

n= int(input())
na = int(input())
li = [int(input()) for _ in range(n-1)]
num = 0
if len(li) == 0:
    print(0)
    exit()

while na <= max(li):
    li.sort()
    li[-1] = li[-1] - 1
    na += 1
    num += 1

print(num)
