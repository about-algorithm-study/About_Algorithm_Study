from collections import deque
 
 
def find_start(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i, j
            
 
for t in range(1, 11):
    T = int(input())
     
    maze = [list(map(int, input().strip())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
    sx, sy = find_start(maze)
 
    direct = deque([(sx, sy)])
    visited[sx][sy] = 1
    result = 0
 
    while direct:
        x, y = direct.popleft()
 
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
 
            if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                if maze[nx][ny] == 3:
                    result = 1
                    found = True
                    break
 
                direct.append((nx, ny))
 
    print(f"#{t} {result}")