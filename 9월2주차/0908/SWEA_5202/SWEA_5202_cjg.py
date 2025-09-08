T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    arr.sort(key=lambda x: x[1])
    cur = 0
    cnt = 0
    for S, E in arr:
        if S >= cur:
            cnt += 1
            cur = E
 
    print(f"#{tc} {cnt}")