T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    check = set()
    count = 0

    while len(check) < 10:
        count += 1
        current_num = count * N
        for i in str(current_num):
            check.add(i)

    print(f"#{tc} {current_num}")
