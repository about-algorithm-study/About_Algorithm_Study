T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    A_total = P * W

    B_total = Q
    if W <= R :
        B_total = Q
    else:
        B_total = Q + (W-R) * S

    if A_total > B_total:
        print(f"#{tc} {B_total}")
    else:
        print(f"#{tc} {A_total}")