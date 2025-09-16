T = int(input())

def subset(index, hap):
    global total

    if hap > K:
        return
    
    if index >= len(nums):
        if hap == K:
            total += 1
        return

    subset(index + 1, hap + nums[index])
    subset(index + 1, hap)

for t in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    
    total = 0
    subset(0, 0)

    print(f"#{t} {total}")