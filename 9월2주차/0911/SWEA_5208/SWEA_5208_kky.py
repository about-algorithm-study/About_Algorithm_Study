T = int(input())

for tc in range(1, T + 1):
    stations = list(map(int, input().split()))
    N = stations[0]
    batteries = stations[1:]

    current_pos = 1
    exchanges = 0

    current_range = current_pos + batteries[0]

    while current_range < N:
        max_reach = current_range
        next_pos = current_pos

        for i in range(current_pos + 1, current_range + 1):
            if i < N:
                reach = i + batteries[i - 1]
                if reach > max_reach:
                    max_reach = reach
                    next_pos = i

        if max_reach <= current_range:
            exchanges = -1
            break

        current_pos = next_pos
        current_range = max_reach
        exchanges += 1

    print(f"#{tc} {exchanges}")
