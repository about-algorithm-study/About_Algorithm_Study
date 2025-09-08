T = int(input())


def subset(num, cnt, hap):
    global total

    if cnt > N and hap > K:
        return 0

    if num > 12:
        if cnt == N and hap == K:
            total += 1
        return
    
    subset(num + 1, cnt, hap)
    subset(num + 1, cnt + 1, hap + num)
    

for t in range(1, T + 1):
    N, K = map(int, input().split())

    total = 0
    subset(1, 0, 0)
    
    print(f"#{t} {total}")