T = int(input())

for t in range(1, T + 1):
    N, M, L = map(int, input().split())

    nodes = [0] * (N + 1)


    for _ in range(M):
        a, b = map(int, input().split())
        nodes[a] = b
    

    for i in range(N, 0, -1):
        left = i * 2
        right = i * 2 + 1
        if left <= N:
            nodes[i] += nodes[left]
        if right <= N:
            nodes[i] += nodes[right]

    print(f"#{t} {nodes[L]}")