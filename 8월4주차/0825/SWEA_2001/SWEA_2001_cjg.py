T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    kill_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for a in range(M):
                for b in range(M):
                    catch += arr[a+i][b+j]
            kill_fly = max(kill_fly, catch)
    print(f'#{tc} {kill_fly}')