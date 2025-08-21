T = int(input())

for t in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()

    size = N // 2

    diff = []

    for i in range(N-1):
        if carrots[i] != carrots[i + 1]:
            diff.append(i)

    min_diff = 10000000
    found = False

    for i in diff:
        for j in diff:

            if i >= j:
                continue

            small = i + 1   # small에 들어갈 개수
            middle = j - i  # j는 포함X
            large = N - j - 1

            if min(small, middle, large) <= 0:
                continue
            if max(small, middle, large) > size:
                continue
            
            found = True
            result = max(small, middle, large) - min(small, middle, large)
            min_diff = min(min_diff, result)
    
    if not found:
        min_diff = -1

    print(f"#{t} {min_diff}")