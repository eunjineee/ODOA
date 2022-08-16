from collections import deque
N, K, M = map(int, input().split())

dd = deque()
num = 0
total =[]
l = -K+1
for i in range(1, N+1):
    dd.append(i)

while True:
    if M-1 >= num % (2*M) >=0 :
        dd.rotate(l)
        total.append(dd.popleft())
        num += 1
    else:
        dd.rotate(-l)
        total.append(dd.pop())
        num += 1
    if len(dd) == 0:
        False
        break
    
for z in total:
    print(z)
