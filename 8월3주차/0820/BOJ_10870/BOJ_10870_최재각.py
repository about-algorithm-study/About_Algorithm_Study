def f(N):

    if N == 0:
        return 0
    if N == 1:
        return  1
    else:
        return f(N-2) + f(N-1) 

N= int(input())
print(f(N))