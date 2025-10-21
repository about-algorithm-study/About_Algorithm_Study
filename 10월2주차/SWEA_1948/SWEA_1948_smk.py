T = int(input())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())

    if m1 == m2:
        print(f"#{t} {d2-d1+1}")
        continue

    day_cnt = 0
    for i in range(m1, m2+1):
        if i == m1:
            day_cnt += days[i] - d1 + 1
        elif i == m2:
            day_cnt += d2
        else:
            day_cnt += days[i]

    print(f"#{t} {day_cnt}")