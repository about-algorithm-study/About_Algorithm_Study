T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(N)]
    hap = []


    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_nums = 0
            for x in range(M):
                for y in range(M):
                    sum_nums += grid[i + x][j + y]
            hap.append(sum_nums)

    max_hap = hap[0]
    for num in hap :
        if num > max_hap :
            max_hap = num

    print(f"#{t} {max_hap}")
