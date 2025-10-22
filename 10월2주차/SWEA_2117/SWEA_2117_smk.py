T = int(input())


def is_in_range(k, x1, y1, x2, y2):
    if abs(x1-x2) + abs(y1-y2) < k:
        return True
    return False

for t in range(1, T + 1):
    N, M = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(N)]
    max_count = -1
    for i in range(N):
        for j in range(N):
            for k in range(1, N + 2):
                cnt = 0
                cost = k*k + (k-1)*(k-1)

                for x in range(N):
                    for y in range(N):
                        if cities[x][y] == 1 and is_in_range(k, i, j, x, y) :
                            cnt += 1
                
                if cnt * M >= cost and cnt >= max_count:
                    max_count = cnt

    print(f"#{t} {max_count}")