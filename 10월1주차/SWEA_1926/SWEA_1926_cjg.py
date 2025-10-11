N = int(input())
for num in range(1, N+1):
    count = str(num).count('3') + str(num).count('6') + str(num).count('9')
    if count > 0:
        print('-' * count, end=' ')
    else:
        print(num, end=' ')