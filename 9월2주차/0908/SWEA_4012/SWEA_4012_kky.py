from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    taste = [list(map(int, input().split())) for _ in range(N)]

    min_diff = float('inf')

    for team_a in combinations(range(N), N//2 ):
        team_b = []
        for i in range(N):
            if i not in team_a:
                team_b.append(i)

        taste_a = 0
        for i in team_a:
            for j in team_a:
                if i != j:
                    taste_a += taste[i][j]

        taste_b = 0
        for i in team_b:
            for j in team_b:
                if i != j:
                    taste_b += taste[i][j]

        diff = abs(taste_a - taste_b)
        min_diff = min(min_diff, diff)
    print(f"#{tc} {min_diff}")