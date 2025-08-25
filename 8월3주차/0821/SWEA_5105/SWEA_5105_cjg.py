from collections import deque
 
def bfs(i, j, N):
    moved = [[0] * N for _ in range(N)]
    q = deque()
    q.append([i, j])
    moved[i][j] = 1
 
    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3: # 도착
            return moved[ti][tj] - 1 - 1
        for di, dj in [(-1,0), (1,0), (0,1), (0, -1)]:
            ni, nj = di+ti, dj+tj
            if 0<= ni < N and 0<= nj < N and maze[ni][nj] != 1 and moved[ni][nj] == 0:
                q.append([ni, nj])
                moved[ni][nj] = moved[ti][tj] + 1
    return 0
 
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')