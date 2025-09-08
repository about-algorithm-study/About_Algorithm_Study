T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    times = []
    for _ in range(N):
        s, e = map(int, input().split())
        times.append((s, e))
        times.sort(key=lambda x: x[1])

    # print(times)
    total = 1
    last_end_time = times[0][1]

    for i in range(1, N):
        start_time, end_time = times[i]

        if start_time >= last_end_time:
            total += 1
            last_end_time = end_time
    print(f"{tc} {total}")
