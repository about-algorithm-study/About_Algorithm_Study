# factorial을 재귀 함수를 사용하여 문제 해결

def fact(N):
    if N <= 1:
        return 1
    else:
        return N * fact(N-1)
    
N = int(input())

result = fact(N)
print(result)