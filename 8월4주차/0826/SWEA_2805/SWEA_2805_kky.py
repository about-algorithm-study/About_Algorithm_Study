T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    numbers = [list(map(int, input())) for _ in range(N)]

    center = N // 2
    total = 0

    for i in range(N):
        distance = abs(i - center)

        start = distance
        end = N - distance

        for j in range(start, end):
            total += numbers[i][j]

    print(f"#{tc} {total}")
