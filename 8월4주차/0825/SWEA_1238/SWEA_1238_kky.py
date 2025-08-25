from collections import deque

T = 10

for tc in range(1, T + 1):
    N, start = map(int, input().split())
    numbers = list(map(int, input().split()))

    graph = {}

    for i in range(0, N, 2): # 2개씩 묶어서 (from, to) 쌍으로 해석
        from_data = numbers[i]
        to_data = numbers[i + 1]

        if from_data not in graph:
            graph[from_data] = []
        if to_data not in graph[from_data]:
            graph[from_data].append(to_data) # from 별로 연결 된 to를 리스트로 저장

    queue = deque([start]) # 큐에 시작점 넣기
    visited = {start} # 이미 연락은 받은 사람들
    last_level = [start] # 마지막에 연락 받는 사람들

    while queue: # 큐가 빌 때까지 반복
        current_level = [] # 새로 연락을 받을 사람들 리스트

        for _ in range(len(queue)):
            current = queue.popleft() # 연락하는 사람

            if current in graph:
                for next_node in graph[current]:
                    if next_node not in visited: # 아직 연락 안 받은 사람이면 연락 받은 사람을 표시하고
                        visited.add(next_node)
                        queue.append(next_node) # 다음에 연락할 사람을 추가
                        current_level.append(next_node) # 이번에 연락받은 사람에 추가


        if current_level: # 이번에 새로 연락받은 사람이 있으면 마지막 레벨 업데이트
            last_level = current_level

    result = max(last_level) # 가장 큰 번호

    print(f"#{tc} {result}")