import sys
sys.stdin = open('5203_input.txt')

def is_babygin(cnt):
    for v in cnt:
        if v >= 3:
            return True
    for i in range(8):
        if cnt[i] and cnt[i+1] and cnt[i+2]:
            return True
    return False

T = int(input())
for tc in range(1, 1+T):
    arr = list(map(int,input().split()))

    p1 = [0] * 10
    p2 = [0] * 10
    ans = 0

    for i in range(0,len(arr),2):

        a = arr[i]
        p1[a] += 1
        if i >= 2 and is_babygin(p1):
            ans = 1
            break

        b = arr[i+1]
        p2[b] += 1
        if i >= 2 and is_babygin(p2):
            ans = 2
            break

    print(p1)
    print(f'#{tc} {ans}')
