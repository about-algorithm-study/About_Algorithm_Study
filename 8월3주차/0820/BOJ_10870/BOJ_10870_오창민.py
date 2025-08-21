#피보나치는 0과 1로 시작 0번째 0 1번째 1, 그다음 2번째는 앞 두 피보나치 수의 합

def fibo(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)


N = int(input())

print(fibo(N))