'''
첫 줄에는 트리의 정점의 총 수 V가 주어짐
다음줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기
간선은 항상 부모- 자식 순서로 표기
'''
def pre_order(t):
    if t:
        print(t, end=' ')
        pre_order(left[t])
        pre_order(right[t])
 
V = int(input())
tree = list(map(int, input().split()))
 
left = [0] * (V + 1)
right = [0] * (V + 1)
par = [0] * (V + 1)
 
for i in range(0, len(tree), 2):
    parent = tree[i]
    child = tree[i+1]
 
    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] = child
 
    par[child] = parent
 
root = 1
for i in range(1, V+1):
    if par[i] == 0:
        root = i
        break
 
pre_order(root)