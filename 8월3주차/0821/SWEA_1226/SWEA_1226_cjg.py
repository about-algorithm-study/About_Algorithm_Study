from collections import deque
 
def bfs(s, N, mase):
 
    boxed = [[0] * 16 for _ in range(16)]
    q = deque()
    q.append((si, sj))
    boxed[si][sj] = 1
    delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while q:
        i, j = q.popleft()
        if maze[i][j] == 3:
            return 1
        for di, dj in delta:
            ni, nj = di +i, dj +j
            if 0<= ni <16 and 0<= nj <16:
                if maze[ni][nj] != 1 and not boxed[ni][nj]:
                    boxed[ni][nj] =1
                    q.append((ni, nj))
    return 0
 
T = 10
for tc in range(1, T+1):
    _ = input().strip()
    maze = [list(map(int, input().strip())) for _ in range(16)]
 
    si = sj = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                si,sj = i, j
    print(f'#{tc} {bfs(si,sj,maze)}')