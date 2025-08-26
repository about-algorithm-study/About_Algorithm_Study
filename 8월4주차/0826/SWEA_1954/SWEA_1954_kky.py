T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    num = 1
    x, y = 0, 0
    direction = 0

    for i in range(N * N):

        arr[x][y] = num
        num += 1

        if i < N * N - 1:

            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                x, y = nx, ny
            else:
                direction = (direction + 1) % 4
                x = x + dx[direction]
                y = y + dy[direction]

    print(f"#{tc}")
    for i in range(N):
        print(*arr[i])
