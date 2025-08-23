import sys
sys.stdin = open('5178_input.txt')

T = int(input())
for tc in range(1,1+T):
    N,M,L = map(int,input().split())
    val = [0]*(N+1)
    for _ in range(M):
        idx, v = map(int,input().split())
        val[idx] = v

    for i in range(N, 0, -1): #완전이진트리 역순
        x, y = 2*i, 2*i + 1  #x:i번 노드의 왼쪽자식, y:i번 노드의 오른쪽 자식
        if x <= N: #왼쪽자식이 트리안에 있으면
            val[i] += val[x] #val[i]에 더함
        if y <= N:
            val[i] += val[y]

    print(f'#{tc} {val[L]}')