T = int(input())

for t in range(1, T + 1):
N = int(input())

price = list(map(int, input().split()))

max_cost = -float('inf')

price = reversed(price)