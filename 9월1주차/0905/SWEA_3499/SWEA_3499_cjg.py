
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input().split()
    # print(arr)

    mid = (N+1)//2
    start = arr[:mid]
    second = arr[mid:]

    result = []
    for i in range(N):
        if i % 2 == 0:
            result.append(start[i//2])
        else:
            result.append(second[i//2])
    print(f"#{tc} {' '.join(result)}")
