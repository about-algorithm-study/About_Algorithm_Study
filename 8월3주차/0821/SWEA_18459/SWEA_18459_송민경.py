from collections import deque

V, E = map(int, input().split())

nums = list(map(int, input().split()))

direct = [[] for _ in range(V + 1)]

for i in range(0, len(nums), 2):
    a = nums[i]
    b = nums[i+1]

    direct[a].append(b)
    direct[b].append(a)

def bfs(start):
    visited = [False] * (V + 1)
    q = deque([start])
    visited[start] = True
    order = []

    while q:
        node = q.popleft()
        order.append(node)
        
        for n in direct[node]:
            if not visited[n]:
                visited[n] = True
                q.append(n)

    return order

result = bfs(1)
print(f"#1", *result)