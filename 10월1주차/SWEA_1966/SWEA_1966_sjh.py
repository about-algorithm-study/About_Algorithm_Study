import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    N = int(input())
    num_li = list(map(int,input().split()))
    result = sorted(num_li)
    print(f'#{tc}',*result)