def dfs(i,j,s,N):
		global minV
		if maze[i][j] == 3:
				if minV > s+1:
						minV = s +1
				return
		else:
				visited[i][j] = 1
				for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
						ni,nj = i + di, j + dj
						if maze[ni][nj] != 1 and visited[ni][nj] == 0:
								dfs(ni,nj,s+1,N)
				visited[i][j] = 0
				return

N, m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]
dfs(sci,scj,0,N)
if minV == N*N:
        minV = -1
print(f'#{tc} {minV}')