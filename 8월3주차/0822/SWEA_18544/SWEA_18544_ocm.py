import sys
sys.stdin = open('input (1).txt')

def preorder(v):
    if v == 0:
        return
    print(v,end=' ')
    preorder(left[v])
    preorder(right[v])

V = int(input())
arr = list(map(int,input().split()))

left = [0]*(V+1)
right = [0]*(V+1)
par = [0]*(V+1)

for i in range(0,len(arr),2):
    p,c = arr[i], arr[i+1]
    par[c] = p
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

root = 0
for v in range(1,1+V):
    if par[v] == 0:
        root = v
        break

preorder(root)