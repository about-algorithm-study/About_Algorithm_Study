T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)
    result = 0
    arr = []
    s = 0

    for i in range(M): #트럭기준으로 돌림
        while s < N and container[s] > truck[i]: #s가 N보다 작고 (i,1),(s,0),(N,3) c[s]가 t[i]보다 클때
            s += 1
        if s < N:
            arr.append(container[s]) # 0이 3보다 작으므로 5추가
            s += 1

    print(f'#{tc}',sum(arr))