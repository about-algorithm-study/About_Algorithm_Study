import sys
sys.stdin = open('input.txt')

"""
원재는 연속되는 N일동안의 가격을 미리 알고 있다
하루에 한개만 구입할 수 있다.
판매는 언제든지 가능
최대 이익을 출력

3
3
10 7 6
3
3 5 9
5
1 1 3 1 2

"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    future = list(map(int,input().split()))
    """
    연속되서 작아지는 경우에는 0을 출력시키는 예외 작성
    연속해서 증가될때까지는 계속 구매 만약 그 다음 값이 작을 경우 판매해서 이익에 추가
    인덱스 N-1이 되면 종료
    """

    if future == sorted(future,reverse=True):
        print(f'#{tc} 0')
        continue

    profit = 0
    max_price = 0

    for i in range(N-1,-1,-1):
        if future[i] > max_price:
            # 오늘이 최고가면 갱신
            max_price = future[i]
        else:
            profit += (max_price - future[i])
    print(f'#{tc} {profit}')
#
# ==================================================================================
# 처음에는 다음날만 보고 계산하는 로직으로 놓치는 케이스들 존재
# import sys
#
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     future = list(map(int, input().split()))
#
#     profit = 0
#
#     # 내림차순이면 0 출력하고 다음 케이스로
#     if future == sorted(future, reverse=True):
#         print(f'#{tc} 0')
#         continue  # 이게 중요!
#
#     buy = []  # 여기로 이동!
#
#     for i in range(N - 1):
#         if future[i] < future[i + 1]:  # 다음날이 더 비싸면 구매
#             buy.append(future[i])
#         else:  # 다음날이 더 싸거나 같으면 판매
#             for price in buy:
#                 profit += (future[i] - price)
#             buy = []  # 판매 후 초기화
#
#     # 마지막 날 처리 (for문이 N-1까지만 돌아서 마지막 날은 안 봄)
#     if buy:  # 아직 안 판 게 있으면
#         for price in buy:
#             profit += (future[N - 1] - price)  # 마지막 날 가격에 판매
#
#     print(f'#{tc} {profit}')
#
