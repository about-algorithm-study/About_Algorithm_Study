T = int(input())

for t in range(1, T + 1):
    N = int(input())

    schedule = [tuple(map(int, input().split())) for _ in range(N)]
    schedule.sort(key= lambda x : x[1])

    cnt = 0
    end = 0

    for x, y in schedule:
        if x >= end:
            cnt += 1
            end = y

    print(f"#{t} {cnt}")
