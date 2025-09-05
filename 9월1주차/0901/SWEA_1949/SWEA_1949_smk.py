def hiking_road(sx, sy, length, k_use):
    global max_len

    max_len = max(max_len, length)

    for dx, dy in delta:
        nx, ny = sx + dx, sy + dy

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if my_map[nx][ny] < my_map[sx][sy] :
                visited[nx][ny] = True
                hiking_road(nx, ny, length + 1, k_use)
                visited[nx][ny] = False
            else:
                if not k_use and my_map[nx][ny] - K < my_map[sx][sy]:
                    curr = my_map[nx][ny]
                    my_map[nx][ny] = my_map[sx][sy] - 1
                    visited[nx][ny] = True
                    hiking_road(nx, ny, length+1, True)
                    visited[nx][ny] = False
                    my_map[nx][ny] = curr



T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]

    start = max(max(row) for row in my_map)
    start_lst = []

    for i in range(N):
        for j in range(N):
            if my_map[i][j] == start:
                start_lst.append((i, j))

    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    max_len = -1

    for x, y in start_lst:
        visited = [[False] * N for _ in range(N)]
        visited[x][y] = True
        hiking_road(x, y, 1, False)
                    
                    
    print(f"#{t} {max_len}")