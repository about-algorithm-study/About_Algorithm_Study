'''
오목 판정
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]

    delta = [(1,0), (1,-1), (0,1), (1,1), (-1,0),(-1,-1),(-1,1),(0,-1)]

    omock = 'NO'

    for i in range(N):
        for j in range(N):
            for di, dj in delta:
                if arr[i][j] == 'o':
                    sum = 1
                    for k in range(1, 5):
                        ni, nj = di*k+i, dj*k+j
                        if 0<= ni<N and 0<= nj < N:
                            if arr[ni][nj] == 'o':
                                sum += 1
                    if sum ==5:
                        omock = 'YES'

    print(f'#{tc} {omock}')