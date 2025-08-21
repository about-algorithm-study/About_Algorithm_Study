from collections import deque


T = int(input())


def find_start(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i, j

for t in range(1, T + 1):
    N = int(input())

    maze = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    sx, sy = find_start(maze)
    
    queue = deque([(sx, sy)])
    visited[sx][sy] = True

    result = 0
    found = False

    while queue:
        x, y = queue.popleft()

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1

                if maze[nx][ny] == 3:
                    found = True
                    result = visited[nx][ny] - 2
                
                queue.append((nx, ny))
        if found:
            break

    print(f"#{t} {result}")