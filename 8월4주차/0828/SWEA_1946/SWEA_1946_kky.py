T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = []
    alphabets = []

    for _ in range(N):
        C, K = map(str, input().split())
        alphabets.append(C * int(K))
        result = "".join(alphabets)

    print(f"#{tc}")
    for i in range(0, len(result), 10):
        print("".join(result[i : i + 10]))
