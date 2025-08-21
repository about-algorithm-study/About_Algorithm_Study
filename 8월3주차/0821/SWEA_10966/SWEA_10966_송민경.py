from collections import deque

T = int(input())


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


for t in range(1, T + 1):
    N, M = map(int, input().split())

    my_map = [list(input().strip()) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]

    queue = deque()

    for i in range(N):
        for j in range(M):
            if my_map[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y +dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    hap = 0
    for i in range(N):
        for j in range(M):
            if my_map[i][j] == 'L':
                hap += visited[i][j]

    print(f"#{t} {hap}")