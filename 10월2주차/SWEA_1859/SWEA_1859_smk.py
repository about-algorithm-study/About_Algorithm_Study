T = int(input())

for t in range(1, T + 1):
    N = int(input())

    price = list(map(int, input().split()))

    max_cost = -float('inf')

    price = reversed(price)
    total_cost = 0

    for i in price:
        max_cost = max(max_cost, i)
        total_cost += max_cost - i
    print(f"#{t} {total_cost}")