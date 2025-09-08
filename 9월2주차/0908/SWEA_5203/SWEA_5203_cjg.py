def baby_gin(player):
    cnt = [0] * 10
    for num in player:
        cnt[num] += 1
 
    for i in range(10):
        if cnt[i] >= 3:
            return True
    for i in range(8):
        if cnt[i] and cnt[i+1] and cnt[i+2]:
            return True
    return False
 
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
 
    result = 0
 
    p1 = []
    p2 = []
    for i in range(12):
        if i % 2 == 1:
            p2.append(arr[i])
            if len(p2) >= 3 and baby_gin(p2):
                result = 2
                break
        else:
            p1.append(arr[i])
            if len(p1) >= 3 and baby_gin(p1):
                result = 1
                break
 
    print(f"#{tc} {result}")