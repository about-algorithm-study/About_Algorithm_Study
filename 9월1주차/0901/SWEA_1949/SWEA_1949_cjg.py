'''
등산로 탐색
'''

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr =[list(map(int, input().split())) for _ in range(N)]

    delta = [(-1,0), (1,0), (0,1), (0,-1)]

    max_cnt = 0
    for i in range(N):
        for j in range(N):
            if max_cnt < arr[i][j]:
                max_cnt = arr[i][j]

                cnt = 0
                for di, dj in delta:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == max_cnt:
                            ans = arr[ni][nj] - K
                            cnt += ans




    print(f"#{tc} {max_cnt}")