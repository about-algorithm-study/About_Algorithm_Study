N = int(input())

for i in range(1, N + 1):
    num_str = str(i)
    count = num_str.count('3') + num_str.count('6') + num_str.count('9')

    print('-' * count if count > 0 else i, end=' ')