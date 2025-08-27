T = int(input())

for tc in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    result_h = h1 + h2
    result_m = m1 + m2

    if result_m > 60:
        result_h += 1
        result_m = result_m - 60
    else:
        result_m = result_m

    if result_h > 12:
        result_h = result_h - 12
    else:
        result_h = result_h

    print(f"#{tc} {result_h} {result_m}")
