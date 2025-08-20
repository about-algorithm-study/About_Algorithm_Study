def fact(N):
    if N == 1:
        return 1
    else:
        return N * fact(N-1)
    
N = int(input())

result = fact(N)
print(result)