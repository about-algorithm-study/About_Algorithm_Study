def fibo(num):
    if num == 1 or num == 2:
        return 1
    elif num == 0:
        return 0
    else:
        return fibo(num - 1) + fibo(num - 2)

N = int(input())
print(fibo(N))