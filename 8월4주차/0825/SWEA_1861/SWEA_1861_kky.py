T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    check = [[0] * N for _ in range(N)]

    def dfs(x, y):
        if check[x][y] != 0:
            return check[x][y]

        check[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if numbers[nx][ny] == numbers[x][y] + 1:
                    check[x][y] = max(check[x][y], 1 + dfs(nx, ny))

        return check[x][y]

    max_count = 0
    start_num = 0

    for i in range(N):
        for j in range(N):
            count = dfs(i, j)

            if count > max_count or (count == max_count and numbers[i][j] < start_num):
                max_count = count
                start_num = numbers[i][j]

    print(f"#{tc} {start_num} {max_count}")