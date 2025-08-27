T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    values = []
    calories = []
    for _ in range(N):
        val, cal = map(int, input().split())
        values.append(val)
        calories.append(cal)

    max_score = 0

    def dfs(idx, current_score, current_caloris):
        global max_score

        if current_caloris > L:
            return

        max_score = max(max_score, current_score)

        if idx == N:
            return

        dfs(idx + 1, current_score + values[idx], current_caloris + calories[idx])

        dfs(idx + 1, current_score, current_caloris)

    dfs(0, 0, 0)

    print(f"#{tc} {max_score}")
