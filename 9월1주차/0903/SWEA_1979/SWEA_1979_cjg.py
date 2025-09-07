T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    max_cnt += 1
                cnt = 0
        if cnt == K:
            max_cnt += 1
        cnt = 0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    max_cnt += 1
                cnt = 0
        if cnt == K:
            max_cnt += 1
        cnt = 0

    print(f"#{tc} {max_cnt}")