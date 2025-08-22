T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [0] * (N+1)

    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(N, 0, -1): # 역순을 처리 > 루트 노드부터 거슬러 올라가며 계산
        left_child = i * 2 # 왼쪽 노드 번호
        right_child = i * 2 + 1 # 오른쪽 노드 번호

        # 자식 노드들이 존재하는 경우 합을 계산
        if left_child <= N:
            tree[i] += tree[left_child]
        if right_child <= N:
            tree[i] += tree[right_child]

    print(f"#{tc} {tree[L]}")
