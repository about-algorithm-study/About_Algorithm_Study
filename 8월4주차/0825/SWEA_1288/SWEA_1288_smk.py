T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num_lst = set()

    num = N
    count = 1

    while len(num_lst) < 10:
        for i in str(num):
            num_lst.add(i)
        if len(num_lst) == 10:
            break
        count += 1
        num = N * count

    print(f"#{t} {num}")

