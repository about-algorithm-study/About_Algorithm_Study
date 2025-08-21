import sys
sys.stdin = open('input.txt')
from collections import deque

# BFS 함수 정의
def bfs(miro):
    escape = False
    # 빈 큐 생성
    q = deque()
    # 시작점(2) 찾기
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                q.append((i,j))
                escape = True
                break
        if escape:
            break
        # 미로 전체 순회
        # 값이 2이면 큐에 좌표 넣고, 더 이상 찾지 않도록 플래그 설정 후 탈출

    # 델타(상하좌우) 정의
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 좌표 꺼내 현재 위치로 사용
        x, y = q.popleft()
        # 네 방향으로 이동
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0<=nx<16 and 0<=ny<16:
                if miro[nx][ny] == 0:
                    miro[nx][ny] = 2
                    q.append((nx,ny))
                elif miro[nx][ny] == 3:
                    return 1
    return 0
            # 경계 체크
            # 길(0)이라면 방문 처리하고 큐에 넣기
            # 도착점(3)이면 1 반환
    # 끝까지 못 가면 0 반환

# 테스트 케이스 수 T = 10
T = 10
# 각 테스트 케이스 반복
for tc in range(1,T+1):
    N = int(input())
    # N 입력 받기
    arr = [list(map(int,input().strip())) for _ in range(16)]
    # 16줄 입력 받아 미로 배열 생성
    ans = bfs(arr)
    # BFS 실행 결과 ans에 저장
    # 결과 출력
    print(f'#{tc} {ans}')