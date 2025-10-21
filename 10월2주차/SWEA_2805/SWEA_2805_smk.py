T = int(input())

for t in range(1, T + 1):
    N = int(input())

    farm = [list(map(int, input().strip())) for _ in range(N)]
    total = 0
    if N == 1:
        total += farm[0][0]
        print(f"#{t} {total}")
        continue

    dist = (N-1)//2

    for i in range(N):
        for j in range(N):
            if abs(i - dist) + abs(j - dist) <= dist:
                total += farm[i][j]
