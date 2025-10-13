# T = 10
#
# for tc in range(1, T + 1):
#     num = int(input())
#     N, M = map(int, input().split())
#
#     result = 1
#     for _ in range(M):
#         result *= N
# print(f"#{num} {result}")

def power(N, M):
    if M == 0:
        return 1

    return N * power(N, M - 1)

T = 10
for tc in range(1, T + 1):
    num = int(input())
    N, M = map(int, input().split())

    result = power(N, M)

    print(f"#{num} {result}")