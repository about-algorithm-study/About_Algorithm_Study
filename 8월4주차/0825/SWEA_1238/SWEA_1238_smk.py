
from collections import deque


for t in range(1, 11):
    N, start = map(int, input().split())
    direct = list(map(int, input().split()))
    road = {}
    for i in range(0, N, 2):
        if direct[i] not in road.keys():
            road[direct[i]] = [direct[i+1]]
        else:
            if direct[i+1] in road[direct[i]]:
                continue
            else:
                road[direct[i]].append(direct[i+1])
    
    visited = [0] * (max(direct) + 1)
    queue = deque([start])
    visited[start] = 1

    while queue:
        now = queue.popleft()
        for next in road.get(now, []):
            if not visited[next]:
                visited[next] = visited[now] + 1
                queue.append(next)

    max_value = max(visited)
    result = -1

    for i in range(len(visited)):
        if visited[i] == max_value:
            result = max(result, i)
    
    print(f"#{t} {result}")