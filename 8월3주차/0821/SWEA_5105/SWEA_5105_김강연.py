from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input())) for _ in range(N)]

    # print(f"=== 테스트 케이스 {tc} ===")
    # print(f"N = {N}")
    # for i, row in enumerate(table):
    #     print(f"행 {i}: {row}")
    # print("========================")


    start_idx = [0, 0]
    end_idx = [0,0]

    for x in range(N):
        for y in range(N):
            if table[x][y] == 2:
                start_idx = [x, y]
            elif table[x][y] == 3:
                end_idx = [x, y]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    visited = [[0] * N for _ in range(N)]

    queue.append((start_idx[0], start_idx[1]))
    visited[start_idx[0]][start_idx[1]] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if(table[nx][ny] == 0 or table[nx][ny] == 3) and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    # print("=== 디버깅 ===")
    # print(f"시작점: {start_idx}")
    # print(f"끝점: {end_idx}")
    # print(f"visited[끝점]: {visited[end_idx[0]][end_idx[1]]}")
    # for row in visited:
    #     print(row)
    # print("===============")

    result = visited[end_idx[0]][end_idx[1]]
    if result > 0:
        print(f"#{tc} {result - 1}")
    else:
        print(f"#{tc} 0")