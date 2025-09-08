T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)

    total = 0

    used = [False] * N

    for i in truck:
        for j in range(N):
            if not used[j] and weight[j] <= i:
                total += weight[j]
                used[j] = True
                break

    print(f"#{t} {total}")