from collections import deque

def bfs(graph, start, goal, V):
    visited = [0] * (V + 1) # 방문 체크 및 거리 저장
    queue = deque([start]) # BFS용 큐, 시작점으로 초기화
    visited[start] = 1 # 시작점을 1로 설정

    while queue:
        current = queue.popleft() # 큐에서 현재 노드 꺼내기

        if current == goal: # 목표지점에 다달했으면
            return visited[current] - 1 # 거리 반환 (1을 빼서 간선 개수로 반환)

        for next_node in graph[current]: # 현재 노드의 모든 인접 노드
            if visited[next_node] == 0: # 아직 방문하지 않았으면
                visited[next_node] = visited[current] + 1 # 거리 업데이트
                queue.append(next_node) # 큐에 추가
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start_node, end_node = map(int, input().split())
        graph[start_node].append(end_node) # start -> end 연결
        graph[end_node].append(start_node) # end -> start 연결

    S, G = map(int, input().split())

    result = bfs(graph, S, G, V)
    print(f"#{tc} {result}")
