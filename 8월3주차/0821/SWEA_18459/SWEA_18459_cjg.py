from collections import deque
def bfs(s, V):                                  # visited -> 방문여부 + 시작 정점에서의 거리 정보를 저장
    visited = [0] * (V+1)                       # 0이면 방문 안한 정점. 1 이상이면 방문했고 거리를 의미
    q = deque()                                  # q는 BFS를 탐색하기 위한 큐, 방문 순서대로 정점을 저장
    q.append(s)                                 # q.append(s), visited[s] = 1 -> 시작 정점을 큐에 넣고 방문 처리
    visited[s] = 1
    while q:                                    # 큐가 빌 때까지 다음 정점을 꺼내서 인접 정점을 탐색
        t = q.popleft()
        print(t, end=' ')
        for w in adj_l[t]:                      # 현재 정점 t에 인접한 정점들을 확인하면서
            if visited[w] == 0:                 # 아직 방문하지 않은 정점만 큐에 넣고 방문처리
                q.append(w)
                visited[w] = visited[t] + 1     # 거리는 부모 정점 거리 + 1
 
V, E = map(int, input().split())        # V는 정점의 개수(1부터 N번 까지 존재)
arr = list(map(int, input().split()))   # E는 간선의 개수
                                        # arr은 간선 정보가 1차원 리스트 형태로 주어짐
adj_l = [[] for _ in range(V+1)]        # adj_l은 인접 리스트로, 각 정점에 연결된 정점들을 저장
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
 
print(f'#1', end=' ')
 
bfs(1, 7)