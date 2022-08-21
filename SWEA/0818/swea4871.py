T = int(input())

for t in range(1,T+1):
    V, E= map(int, input().split())
    adjlist = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjlist[a].append(b)
    s, g = map(int, input().split())
    visited = [0] * (V+1)
    stack = [0] * (V+1)
    top = -1
    visited[s] = 1
    while True:
        for daum in adjlist[s]:
            if visited[daum] == 0:
                top += 1
                stack[top] = s
                s = daum
                visited[daum] = 1
                break
        else:
            if top != -1:
                s = stack[top]
                top -= 1
            else:
                break
    if visited[g] == 1 :
        to = 1
    else:
        to = 0
    print(f'#{t} {to}')
'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''