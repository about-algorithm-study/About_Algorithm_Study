T = int(input())

def comp_a(amount, p):
    return amount * p

def comp_b(amount, q, r, s):
    if amount <= r:
        return q
    else:
        return q + (amount-r) * s

for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    result = min(comp_a(W, P), comp_b(W, Q, R, S))
    print(f"#{t} {result}")