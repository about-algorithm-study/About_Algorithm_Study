import sys
sys.stdin = open('sample_input.txt')
"""
#우리가 고려해야할 부분
어떤 크기로 서비스를 제공할 것인가 ->k 모든 경우의 수를 탐색해야하니 함수자체를 for문돌려서 찾아본다. distance가 0이되면안되니 1부터
집을 최대한 포함시킬 수 있는 케이스를 찾아야한다. 
운영비용보다 이익이 작으면 안된다 -> if cnt*M - (k**2 + (k-1)**2) >= 0 and cnt > max_home:
"""


def finding(k):
    global max_home
    distance = k-1

    for i in range(N):
        for j in range(N):
            #기준값을 하나하나 정해서 거리별로 확인
            center = (i,j)
            cnt = 0
            for x in range(N):
                for y in range(N):
                   if abs(center[0]-x)+abs(center[1]-y)<=distance and home_position[x][y]==1:
                       cnt += 1
            if cnt*M - (k**2 + (k-1)**2) >= 0 and cnt > max_home:
                max_home = cnt



T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    #하나의 집이 낼 수 있는 비용 M

    home_position = [list(map(int,input().split())) for _ in range(N)]
    #회사가 무조건 드는 운영비용은 고정
    # 1, 5, 13, 25,
    # 1, 4 + 1, 9 + 4, 16 + 9,

    # K를 구해야하고 그 안에 집이 최대한 많이 포함되게
    #회사의 이익은
    # M * 최대한 많은 집 - 운영비용
    max_home = 0

    for i in range(1,N+2):
        finding(i)

    print(f'#{tc} {max_home}')