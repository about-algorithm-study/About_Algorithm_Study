def backtrack(idx, cost):
    global min_cost
    if idx == N:
        min_cost = min(min_cost, cost)
        return

    if cost >= min_cost:
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = True
            backtrack(idx + 1, cost + arr[idx][j])
            visited[j] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_cost = float('inf')
    visited = [False] * N
    backtrack(0, 0)

    print(f"#{tc} {min_cost}")
