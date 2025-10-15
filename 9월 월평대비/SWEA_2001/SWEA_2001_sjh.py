"""
파리퇴치
M크기의 파리채로 최대한 많이 죽인 수 출력
"""

import sys
sys.stdin = open('input.txt')
def killing(x, y):
    global max_kill
    result = 0

    for nx in range(x, x + M):
        for ny in range(y, y + M):
            result += arr[nx][ny]

    max_kill = max(result, max_kill)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 시작점 설정 전부 탐색시
            killing(i, j)

    print(f'#{tc} {max_kill}')