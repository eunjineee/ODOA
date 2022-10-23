from pprint import pprint
import heapq
import sys
input = sys.stdin.readline

def f(start):                                             #다익스트라 사용하기
    q = []
    heapq.heappush(q,(start, 0))
    visited[start] = 0
    while q:
        now, time = heapq.heappop(q)
        if visited[now] < time:
            continue
        if now in wiredi.keys() and len(wiredi[now]) != 0:
            for (node, node_time) in wiredi[now]:
                next_time = time + node_time
                if next_time < visited[node]:
                    visited[node] = next_time
                    heapq.heappush(q, (node, next_time))

plant, wire = map(int,input().split())
minwire = float(input().rstrip())

plantdi = {}                                            #공장 위치(x,y)를 딕셔너리로 받음
for i in range(1, plant+1):
    x, y = map(int,input().split())
    plantdi[i] = (x,y)
<<<<<<< HEAD
print(f'plantdi:')
pprint(plantdi)
=======
# print(f'plantdi:')
# pprint(plantdi)
>>>>>>> 2a84d7e9530aaf8c23ec97412a5affe040c2223d

wiredi = {}
for j in range(1, plant+1):
    wiredi[j] = []

for _ in range(wire):                                  #이미 연결된 공장들은 거리를 0으로 넣어줌
    a, b = map(int, input().split())                   #양방향으로 넣어줘야함***ㅠㅜㅠ
    wiredi[a].append((b,0))
    wiredi[b].append((a,0))
<<<<<<< HEAD
print(f'wiredi:')
pprint(wiredi)
=======
# print(f'wiredi:')
# pprint(wiredi)
>>>>>>> 2a84d7e9530aaf8c23ec97412a5affe040c2223d

for aa in range(1,plant+1):                            #연결되지 않은 부분은 최대길이를 넘지않을때 추가
    for bb in range(aa+1,plant+1):
        wirelen = (abs(plantdi[bb][0]-plantdi[aa][0])**2 + abs(plantdi[bb][1]-plantdi[aa][1])**2 )**(0.5)
        if wirelen <= minwire:
                wiredi[aa].append((bb, wirelen))
                wiredi[bb].append((aa, wirelen))
<<<<<<< HEAD
print(f'wiredi:')
pprint(wiredi)
=======
# print(f'wiredi:')
# pprint(wiredi)
>>>>>>> 2a84d7e9530aaf8c23ec97412a5affe040c2223d

INF = sys.maxsize
visited = [INF] * (plant + 1)                           #다익스트라에서 최소 찾기니까 inf로 만들어주기

f(1)

<<<<<<< HEAD
pprint(visited)
=======
# pprint(visited)
>>>>>>> 2a84d7e9530aaf8c23ec97412a5affe040c2223d
print(int(visited[plant] * 1000))