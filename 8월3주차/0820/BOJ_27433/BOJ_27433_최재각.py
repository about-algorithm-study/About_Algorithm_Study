N = int(input())

def f(N):       # 함수 만들어주기

    factorial = 1   # 팩토리얼 N값부터 1까지 곱하기여서 기본 1로 주기
    
    for fac in range(1, N+1):       # 범위는 1부터 N+1 그래야 N값까지 가능
    
        factorial *= fac        # for문을 돌면서 fac 값을 계속 곱해주기 N번까지
    
    return factorial        # factorial로 돌아가서 계속곱해주기

print(f(N))     # 함수 출력해주기