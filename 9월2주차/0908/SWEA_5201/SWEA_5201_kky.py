T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    total = 0
    used_truck = []

    for container in containers:
        for truck_idx in range(len(trucks)):
            if truck_idx in used_truck:
                continue

            if trucks[truck_idx] >= container:
                total += container
                used_truck.append(truck_idx)
                break

    print(f"#{tc} {total}")
