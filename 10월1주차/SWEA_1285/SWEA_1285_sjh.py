import sys
sys.stdin = open('input (1).txt')

def finding(N, position):
    close_stone = 1000000
    cnt = 0
    for i in range(N):
        distance = abs(position[i] - 0)

        if distance < close_stone:
            close_stone = distance
            cnt =1
        elif distance == close_stone:
            cnt += 1
    return close_stone, cnt


T=int(input())
for tc in range(1,T+1):
    N = int(input()) #N명의 사람
    #원하는 지점에 최대한 가깝게 돌 던지기
    position = list(map(int,input().split()))
    # -100,000 ~ 100,000 숫자가 일렬로 써져있다. 100,000위치에서
    #0에 최대한 가까운 위치로 던지려고 한다.
    # 떨어진 위치와 0사이의 거리, 몇명이 던졌는지 출력( 가장 가까이)

    result = finding(N,position)
    print(f'#{tc} {result[0]} {result[1]}')
