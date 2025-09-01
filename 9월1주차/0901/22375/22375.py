T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    first = list(map(int, input().split()))
    end = list(map(int, input().split()))

    current = first[:]
    switches = 0

    for i in range(N):
        if current[i] != end[i]:
            switches += 1

            for j in range(i, N):
                current[j] = 1 - current[j]

    print(f"#{tc} {switches}")