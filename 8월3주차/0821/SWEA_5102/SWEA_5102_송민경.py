from collections import deque


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())

    directions = [[] for _ in range(V + 1)]

    visited = [0] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        directions[a].append(b)
        directions[b].append(a)

    S, G = map(int, input().split())

    queue = deque([S])
    visited[S] = 0

    while queue:

        x = queue.popleft()

        for num in directions[x]:
            if visited[num]==0 and num != S:
                visited[num] = visited[x] + 1
                queue.append(num)


    result = visited[G] if visited[G] > 0 else 0
    print(f"#{t} {result}")