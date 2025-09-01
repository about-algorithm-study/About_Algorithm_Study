'''
파리퇴치 3
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    delta1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    delta2 = [(-1, 1), (-1, -1), (1, -1), (1, 1)]

    max_cns = 0
    for i in range(N):
        for j in range(N):
            cns = arr[i][j]
            for di, dj in delta1:
                for k in range(1,M):
                    ni, nj = di * k + i, dj * k + j
                    if 0 <= ni < N and 0<= nj < N:
                        cns += arr[ni][nj]
                        max_cns = max(max_cns,cns)

            ans = arr[i][j]
            for di, dj in delta2:
                for k in range(1, M):
                    ni, nj = di * k + i, dj * k +j
                    if 0 <= ni < N and 0<= nj < N:
                        ans += arr[ni][nj]
                        max_cns = max(max_cns,ans)
    print(f"#{tc} {max_cns}")