T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    matrix_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_90[i][j] = numbers[N - 1 - j][i]

    matrix_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_180[i][j] = numbers[N - 1 - i][N - 1 - j]

    matrix_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix_270[i][j] = numbers[j][N - 1 - i]

    print(f"#{tc}")
    for i in range(N):
        row_90 = "".join(map(str, matrix_90[i]))
        row_180 = "".join(map(str, matrix_180[i]))
        row_270 = "".join(map(str, matrix_270[i]))

        print(row_90, row_180, row_270)
