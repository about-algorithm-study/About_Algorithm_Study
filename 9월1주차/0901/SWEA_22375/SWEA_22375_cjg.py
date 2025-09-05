
'''
N개의 전등 1번부터 N번 1번을 조작하면 i번부터 N번까지의 전들이 켜짐/꺼짐이 반대가 됨
최소 몇개의 스위치를 조작해야할지

켜진 상태는 1, 꺼진 상태는 0
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cns = 0
    for i in range(N):
        if A[i] != B[i]:
            cns += 1
            for j in range(N):
                A[j] = 1 - A[j]

    print(f'#{tc} {cns}')