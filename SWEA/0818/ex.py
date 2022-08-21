def dfs(v, N):
    visited = [0] * N   # visited 생성
    stack = [0] * N     # stack 생성
    top = -1
    print(v)
    visited[v] = 1 # 시작점 방문 표시
    while True:
        for w in adjList[v]:
            if visited[w] == 0: # if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
                top += 1
                stack[top] = v  # push(v)
                v = w           # v <- w (w에 방문)
                print(v) # 방문
                visited[w] = 1  # visited[w] <- true
                break
        else:                   # w가 없으면
            if top != -1:# 스택이 비어있지 않은 경우
                v = stack[top]  # pop
                top -= 1
            else:               # 스택이 비어있으면
                break