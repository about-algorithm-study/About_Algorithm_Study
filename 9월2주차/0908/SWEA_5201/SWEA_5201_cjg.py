T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    con_weight = list(map(int, input().split()))
    tru_weight = list(map(int, input().split()))
 
    con_weight.sort(reverse=True)
    tru_weight.sort(reverse=True)
 
    max_con = 0
    con_idx = 0
    for truck in tru_weight:
        while con_idx < N:
            if con_weight[con_idx] <= truck:
                max_con += con_weight[con_idx]
                con_idx += 1
                break
            else:
                con_idx += 1
    print(f"#{tc} {max_con}")