import sys
sys.stdin = open('input.txt')

""""
농장의 규칙
농장의 크기는 항상 홀수
수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 모양만 가능
수익은 해당 칸의 값을 다 더함
마름모를 어떻게 구현할 것인지? => 거리계산으로 중심값부터 거리가 N이하인 경우
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    center_x, center_y = (N-1)//2, (N-1)//2


    distance = N // 2
    profit = 0
    for i in range(N):
        for j in range(N):
            if abs(i-center_x)+abs(j-center_y)<=distance:
                profit += farm[i][j]

    print(f'#{tc} {profit}')