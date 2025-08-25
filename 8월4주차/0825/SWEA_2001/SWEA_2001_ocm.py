T = int(input())

for tc in range(1,1+T):

    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    maxkill = 0
    for i in range(N):
        for j in range(N):
            s = 0
            for r in range(M):
                for c in range(M):
                    di,dj = i+r, j+c
                    if 0<=di<N and 0<=dj<N:
                        s+=arr[di][dj]
                        if maxkill < s:
                            maxkill = s
    print(f'#{tc}', maxkill)