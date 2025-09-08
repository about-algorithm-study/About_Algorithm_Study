T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])
    cnt = 0
    end = 0

    for s, e in arr:
        if s >= end:
            cnt += 1
            end = e

    print(f'#{tc}', cnt)