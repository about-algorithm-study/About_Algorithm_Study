
T = 10
N = 100
for tc in range(1, T+1):
    _ = input()
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            cnt += arr[i][j]
        max_cnt = max(max_cnt, cnt)

    for j in range(N):
        ans = 0
        for i in range(N):
            ans += arr[i][j]
        max_cnt = max(max_cnt, ans)

    bns = 0
    for i in range(N):
        bns += arr[i][i]
    max_cnt = max(max_cnt, bns)

    cns = 0
    for i in range(N):
        cns = arr[i][N-i-1]
        max_cnt = max(max_cnt, cns)

    print(f"#{tc} {max_cnt}")