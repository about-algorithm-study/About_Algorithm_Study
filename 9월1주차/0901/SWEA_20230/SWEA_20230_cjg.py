
'''
풍선팡 2
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]
            for k in range(1, N):
                for di, dj in delta:
                    ni, nj = di * k + i, dj * k + j
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
                        max_cnt = max(max_cnt,cnt)
    print(f'#{tc} {max_cnt}')