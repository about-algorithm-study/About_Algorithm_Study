import sys
sys.stdin = open('input.txt')
'''
하루 최대 한개 구입 가능 판매 언제든 가능
최대 이익
3 5 9 -> -3 -5 +18
          1  1  -2
1 1 3 1 2 -> -1 -1 +6 -1 +2
              1  1 -2  1 -1

6 7 10
9 5 3
2 1 3 1 1
'''
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int,input().split()))[::-1]
    answer = 0
    result = 0

    for val in arr:
        if val >= answer:
            answer = val
        else:
            result += answer - val
    print(result)