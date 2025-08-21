from collections import deque

T = 10

for _ in range(1, T+1):
    tc = int(input())
    table = [list(map(int, input())) for _ in range(16)]

    start_idx = [0, 0]
    end_idx = [0, 0]

    for x in range(16):
        for y in range(16):
            if table[x][y] == 2:
                start_idx = [x, y]
            elif table[x][y] == 3:
                end_idx = [x, y]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    visited = [[False] * 16 for _ in range(16)]

    queue.append((start_idx[0], start_idx[1]))
    visited[start_idx[0]][start_idx[1]] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 16 and 0 <= ny < 16:
                if (table[nx][ny] == 0 or table[nx][ny] == 3) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    if visited[end_idx[0]][end_idx[1]]:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")