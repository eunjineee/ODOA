'''
9
7 4 2 0 0 6 0 7 0
최대값의 위치, 같은 값이 있을때는 맨 오른쪽꺼
'''

N = int(input())
arr = list(map(int, input().split()))

#거품정렬
for i in range(N-1,0,-1):
    for j in range(i):
        if arr[j] > arr [j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

#카운트 정렬
tmp = [0] * N
c = [0] * 101
for i in range(N):
    c[arr[i]] += 1
for j in range(1, 101):
    c[j] += c[j-1]
for i in range(N-1,-1,-1):
    c[arr[i]] -= 1
    tmp[c[arr[i]]] = arr[i]
print(tmp)