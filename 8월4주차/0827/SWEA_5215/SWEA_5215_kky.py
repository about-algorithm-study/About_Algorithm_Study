T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    values = []
    calories = []
    for _ in range(N):
        val, cal = map(int, input().split())
        values.append(val)
        calories.append(cal)

    max_score = 0

    def dfs(idx, current_score, current_caloris):
        global max_score

        if current_caloris > L:
            return

        max_score = max(max_score, current_score)

        if idx == N:
            return

        dfs(idx + 1, current_score + values[idx], current_caloris + calories[idx])

        dfs(idx + 1, current_score, current_caloris)

    dfs(0, 0, 0)

    print(f"#{tc} {max_score}")

"""
# dfs를 deque를 이용해서 풀이하는 방법
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    values = []
    calories = []
    for _ in range(N):
        val, cal = map(int, input().split())
        values.append(val)
        calories.append(cal)

    max_score = 0
    
    # deque에 (idx, current_score, current_calorie) 형태로 저장
    stack = deque()
    stack.append((0, 0, 0))  # 시작점
    
    while stack:
        idx, current_score, current_calorie = stack.pop()
        
        # 칼로리 제한 초과시 건너뛰기
        if current_calorie > L:
            continue
        
        # 최대 점수 갱신
        max_score = max(max_score, current_score)
        
        # 모든 재료를 확인했으면 다음으로
        if idx == N:
            continue
        
        # 현재 재료를 선택하지 않는 경우
        stack.append((idx + 1, current_score, current_calorie))
        
        # 현재 재료를 선택하는 경우
        stack.append((idx + 1, current_score + values[idx], current_calorie + calories[idx]))
    
    print(f"#{tc} {max_score}")
    """
