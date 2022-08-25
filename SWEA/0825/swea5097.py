from collections import deque
T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    nums = deque(map(int,input().split()))
    nums.rotate(-m)
    print(f'#{t+1} {nums.popleft()}')
