def backtracking(product, current_cost, used_plant):
    global min_cost

    if product == N:
        min_cost = min(min_cost, current_cost)
        return

    if current_cost >= min_cost:
        return

    for plant in range(N):
        if not used_plant[plant]:
            used_plant[plant] = True
            cost = costs[product][plant]
            backtracking(product + 1, current_cost + cost, used_plant)

            used_plant[plant] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]

    min_cost = float("inf")
    used_plant = [False] * N

    backtracking(0, 0, used_plant)

    print(f"#{tc} {min_cost}")
