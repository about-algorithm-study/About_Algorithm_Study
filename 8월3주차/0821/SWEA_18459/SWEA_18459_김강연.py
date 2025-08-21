from collections import deque

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
edge = list(map(int, input().split()))

for i in range(0, len(edge), 2):
    u = edge[i]
    v = edge[i+1]
    A[u].append(v)
    A[v].append(u)

def BFS(v):
    visited = [0] * (N + 1)
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.popleft()
        print(t, end=" ")
        for i in A[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1


print("#1", end=" ")
BFS(1)
print()
