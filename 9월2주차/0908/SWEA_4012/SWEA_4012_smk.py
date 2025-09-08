def synergy(lst):
    total = 0

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            a, b = lst[i], lst[j]
            total += ingredient[a][b] + ingredient[b][a]

    return total


def find_case(idx, choosed):
    global min_diff

    if len(choosed) == N // 2:
        other = [i for i in range(N) if i not in choosed]
        s1 = synergy(choosed)
        s2 = synergy(other)
        min_diff = min(min_diff, abs(s1-s2))
        return
    
    if idx >= N:
        return
    
    find_case(idx + 1, choosed + [idx])
    find_case(idx + 1, choosed)


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    ingredient = [list(map(int, input().split())) for _ in range(N)]
    min_diff = 1000000000

    find_case(0, [])

    print(f"#{t} {min_diff}")