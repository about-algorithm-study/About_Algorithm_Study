def fact(n):
    if n - 1 == 0 or n == 0: # N의 범위를 볼필요가 있다 0 처리안하면 런타임에러
        return 1
    else:
        return n * fact(n - 1)

N = int(input())

print(fact(N))