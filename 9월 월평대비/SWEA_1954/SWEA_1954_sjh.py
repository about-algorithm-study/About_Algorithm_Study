import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    max_num = N**2

    #시계방향순으로 정의해두기
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    #시작점 설정
    x,y = 0,0
    d = 0

    for num in range(1, max_num+1):
        arr[y][x] = num

        # 마지막 숫자는 탐색할 필요 없으니까
        if num < max_num :
            nx = x + dx[d]
            ny = y + dy[d]

            #방향전환의 조건
            if not(0<=nx<N and 0<=ny<N) or arr[ny][nx] != 0:
                d = (d + 1) % 4
                nx = x + dx[d]
                ny = y + dy[d]

            x,y = nx,ny

    print(f'#{tc}')
    for row in arr:
        print(*row)