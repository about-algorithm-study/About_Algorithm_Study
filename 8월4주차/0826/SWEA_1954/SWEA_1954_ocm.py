import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    lst = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1] #우,하,좌,상
    dy = [1, 0, -1, 0]
    x, y = 0, 0 #시작좌표
    d = 0 # d=0 우 d=1 아래 ...

    for i in range(1,N*N+1):
        lst[x][y] = i #현재 칸에 숫자 넣기

        #다음 위치 계산
        nx = x + dx[d]
        ny = y + dy[d]

        #배열범위를 벗어남 or 이미 숫자가 채워져 있음 -> 방향 바꾸기
        if nx < 0 or nx >= N or ny <0 or ny >= N or lst[nx][ny] != 0:
            d = (d + 1) % 4 # %4를 붙여 0~3 사이 반복 되게 만듦
            nx = x + dx[d] #새로운 방향으로 다시 한칸 이동 좌표 계산
            ny = y + dy[d]
        x, y = nx, ny #좌표 이동
    for row in lst:
        print(*row)