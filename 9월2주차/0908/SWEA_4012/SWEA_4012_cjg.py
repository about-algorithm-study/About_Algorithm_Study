
def synergy(num):
    total = 0
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            food1 = num[i]
            food2 = num[j]
            total += arr[food1][food2] + arr[food2][food1]
    return total

def combination(idx, goso):
    global min_diff

    if len(goso) == (N//2):
        other = [i for i in range(N) if i not in goso]
        s1 = synergy(goso)
        s2 = synergy(other)
        result = abs(s1-s2)
        min_diff = min(min_diff,result)
        return

    if idx >= N:
        return

    combination(idx+1, goso + [idx])
    combination(idx+1, goso)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_diff = float('inf')

    combination(0,[])
    print(f"#{tc} {min_diff}")